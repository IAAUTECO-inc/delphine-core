import json
import uuid
from datetime import datetime, UTC
import os

def parse_requirements(file_path):
    dependencies = []
    if not os.path.exists(file_path):
        print(f"Warning: {file_path} not found.")
        return dependencies

    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if line.startswith('-r'):
                # Handle recursive requirements
                base_dir = os.path.dirname(file_path)
                sub_req = os.path.join(base_dir, line.split()[1])
                dependencies.extend(parse_requirements(sub_req))
                continue
            
            # Basic parsing for package==version
            parts = line.split('==')
            if len(parts) == 2:
                dependencies.append({
                    "name": parts[0],
                    "version": parts[1]
                })
            elif '>=' in line:
                 parts = line.split('>=')
                 dependencies.append({
                    "name": parts[0],
                    "version": parts[1]
                })
            else:
                # Handle other cases or unpinned deps if necessary
                # For now, just taking the name if possible
                name = line.split('[')[0].split('<')[0].split('>')[0].split('=')[0]
                dependencies.append({
                    "name": name,
                    "version": "unknown"
                })
    return dependencies

def generate_cyclonedx_sbom(dependencies):
    sbom = {
        "bomFormat": "CycloneDX",
        "specVersion": "1.4",
        "serialNumber": f"urn:uuid:{uuid.uuid4()}",
        "version": 1,
        "metadata": {
            "timestamp": datetime.now(UTC).isoformat(),
            "tools": [
                {
                    "vendor": "KoalixCRM",
                    "name": "SBOM Generator",
                    "version": "1.0"
                }
            ],
            "component": {
                "type": "application",
                "name": "KoalixCRM",
                "version": "1.0.0" 
            }
        },
        "components": []
    }

    for dep in dependencies:
        component = {
            "type": "library",
            "name": dep['name'],
            "version": dep['version'],
            "purl": f"pkg:pypi/{dep['name']}@{dep['version']}"
        }
        sbom['components'].append(component)

    return sbom

if __name__ == "__main__":
    requirements_file = os.path.join(os.path.dirname(__file__), '../requirements/production_requirements.txt')
    # Resolve absolute path
    requirements_file = os.path.abspath(requirements_file)
    
    print(f"Parsing requirements from: {requirements_file}")
    dependencies = parse_requirements(requirements_file)
    
    sbom = generate_cyclonedx_sbom(dependencies)
    
    output_file = os.path.join(os.path.dirname(__file__), '../sbom.json')
    with open(output_file, 'w') as f:
        json.dump(sbom, f, indent=4)
    
    print(f"SBOM generated at: {output_file}")
    print(f"Found {len(dependencies)} dependencies.")
