# KoalixCRM

## Overview
## DELPHINE ## is the database and critical data management system (CRM) at the core of the Winterhold ecosystem. It is the most ethical, secure, and auditable solution for any organization handling sensitive records (social assistance, health, or personal information).

Our mission is to guarantee that critical data remains sovereign and serves only one purpose: the autonomy and integrity of the end-user.

## Architecture

- **Database**: PostgreSQL

## Features
## DELPHINE ## is optimized to securely and efficiently feed complex AI models across the Winterhold architecture (Skald, DAWNSTAR, ESBERN).

Polyglot Storage: We utilize polyglot database systems (SQL, NoSQL, Graph) to optimize information extraction and specialized querying by AI models.
Native Deep Learning Integration: DELPHINE is structured for efficient access by models:
PyTorch / Keras: Used for needs segmentation and predictive risk analysis based on assistance profiles.
Scikit-learn: Used for lightweight classification and detecting anomalies in data entries.
Secure Extraction API (for MASAQ): A specially designed API ensures that the MASAQ engine can extract the necessary data for the Skald Agent's inference without compromising the integrity of the entire dataset.
## Installation (Development)
1. Install Python 3.10+
2. Install PostgreSQL and create a database for the project.
3. Configure the database connection in `projectsettings/settings.py`.
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the database migrations:
    ```bash
    python manage.py migrate
    ```
6. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Documentation
The documentation for the project can be found [here](http://readthedocs.org/docs/koalixcrm/en/master/).

## FreeBSD Service
To run KoalixCRM as a service on FreeBSD, you can use the provided rc.d script template.

1. Copy the script template to the rc.d directory:
    ```bash
    cp scripts/koalixcrm.in /usr/local/etc/rc.d/koalixcrm
    ```
2. Make the script executable:
    ```bash
    chmod +x /usr/local/etc/rc.d/koalixcrm
    ```
3. Edit the script to set the correct values for the following variables:
    - `koalixcrm_user`
    - `koalixcrm_group`
    - `koalixcrm_dir`
4. Enable the service in `/etc/rc.conf`:
    ```bash
    echo 'koalixcrm_enable="YES"' >> /etc/rc.conf
    ```
5. Start the service:
    ```bash
    service koalixcrm start
    ```
