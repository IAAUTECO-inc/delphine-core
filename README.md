# KoalixCRM

## Overview
KoalixCRM is a Django-based web application for small business management.

## Architecture
- **Framework**: Django
- **Database**: PostgreSQL

## Features
- Manage Contacts, Customers, Suppliers
- Create and Manage Quotes, Invoices, Purchase Orders
- Product and Price Management
- PDF Document Generation
- Double Entry Accounting

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