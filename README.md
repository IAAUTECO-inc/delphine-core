# KoalixCRM - Desktop Edition

## Overview
KoalixCRM is being reimagined as a high-performance desktop application for small business management.
**Note**: This project is currently migrating from a Django-based web application to a standalone desktop application using **Qt (PySide6)** and **PostgreSQL**.

## Architecture
- **User Interface**: PySide6 (Qt for Python)
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Architecture Diagram**: See [architecture.mermaid](architecture.mermaid)

## Features (Planned)
- Manage Contacts, Customers, Suppliers
- Create and Manage Quotes, Invoices, Purchase Orders
- Product and Price Management
- PDF Document Generation
- Double Entry Accounting

## Installation (Development)
1. Install Python 3.10+
2. Install PostgreSQL
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python main.py
   ```

## Documentation
Legacy documentation for the Django version can be found [here](http://readthedocs.org/docs/koalixcrm/en/master/).
New documentation will be added as the migration progresses.
