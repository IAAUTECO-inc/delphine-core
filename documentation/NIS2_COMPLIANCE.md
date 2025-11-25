# NIS2 Compliance Documentation - KoalixCRM

## 1. Introduction
This document outlines the technical and organizational measures implemented in KoalixCRM to align with the **NIS2 Directive (EU 2022/2555)**. While KoalixCRM is a desktop application, this documentation serves to demonstrate security preparedness and risk management for entities using this software.

## 2. Risk Analysis and Information System Security Policies
**Objective:** Identify and mitigate risks to the confidentiality, integrity, and availability of data.

*   **Asset Inventory:** All critical assets (Customer Data, Financial Records) are stored in a centralized PostgreSQL database.
*   **Threat Modeling:** Regular assessment of threats such as unauthorized access, data loss, and malware.
*   **Access Control:**
    *   Role-Based Access Control (RBAC) implemented within the application.
    *   Database access restricted to authenticated users/applications.

## 3. Incident Handling
**Objective:** Ensure prompt detection, analysis, and reporting of security incidents.

*   **Detection:** Logging of all critical actions (login attempts, data modification) to local audit logs.
*   **Reporting:** Users are provided with a mechanism to report bugs and security vulnerabilities via GitHub Issues (private reporting channel recommended for vulnerabilities).
*   **Response Plan:**
    1.  Isolate the affected system.
    2.  Analyze the breach (logs, database).
    3.  Patch the vulnerability.
    4.  Notify affected parties (if personal data is compromised, GDPR notification procedures apply).

## 4. Business Continuity and Crisis Management
**Objective:** Ensure capability to restore data and operations after an incident.

*   **Backup Strategy:**
    *   Automated daily backups of the PostgreSQL database.
    *   Backups encrypted and stored in a separate location (off-site/cloud).
*   **Disaster Recovery:**
    *   Documentation provided for restoring the database from backups.
    *   Application installer available for rapid redeployment.

## 5. Supply Chain Security
**Objective:** Manage risks stemming from third-party dependencies.

*   **Dependency Management:**
    *   Strict pinning of Python package versions in `requirements.txt`.
    *   Regular automated scanning of dependencies for known vulnerabilities (e.g., using `pip-audit` or GitHub Dependabot).
*   **Vendor Assessment:** Evaluation of the security posture of critical libraries (Qt, SQLAlchemy).

## 6. Cryptography and Encryption
**Objective:** Protect data at rest and in transit.

*   **Data in Transit:**
    *   PostgreSQL connections configured to enforce **SSL/TLS**.
*   **Data at Rest:**
    *   Recommendation to use Full Disk Encryption (BitLocker/FileVault) on host machines.
    *   Sensitive fields (passwords) hashed using strong algorithms (Argon2/bcrypt) before storage.

## 7. Vulnerability Handling and Disclosure
**Objective:** Systematically manage software vulnerabilities.

*   **Patch Management:** Regular release cycles to address discovered vulnerabilities.
*   **Disclosure Policy:** Clear guidelines for security researchers to report vulnerabilities responsibly.

## 8. HR Security and Training
**Objective:** Ensure personnel are aware of cybersecurity risks.

*   **Training:** Developers trained in secure coding practices (OWASP Top 10).
*   **Access Reviews:** Periodic review of developer access rights to the codebase and release infrastructure.
