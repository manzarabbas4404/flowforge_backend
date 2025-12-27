FlowForge Backend

[![Python Version](https://img.shields.io/badge/python-3.13%2B-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/django-4.x-green)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/djangorestframework-latest-orange)](https://www.django-rest-framework.org/)
[![License](https://img.shields.io/badge/license-MIT-lightgrey)](LICENSE)

> **FlowForge** is a **multi-tenant, API-first workflow & task management backend** built with **Django + Django REST Framework**, designed to demonstrate **production-grade architecture, performance optimization, and DevOps readiness**.

---

## Table of Contents

* [About the Project](#about-the-project)
* [Key Features](#key-features)
* [Tech Stack](#tech-stack)
* [Architecture Overview](#architecture-overview)
* [Prerequisites](#prerequisites)
* [Getting Started](#getting-started)

  * [Clone the Repository](#clone-the-repository)
  * [Environment Variables](#environment-variables)
  * [Install Dependencies](#install-dependencies)
  * [Database Setup & Migrations](#database-setup--migrations)
  * [Run the Development Server](#run-the-development-server)
* [API Endpoints](#api-endpoints)
* [Authentication](#authentication)
* [Query Optimization Notes](#query-optimization-notes)
* [CI/CD Overview](#cicd-overview)
* [Deployment (Planned)](#deployment-planned)
* [Project Goals](#project-goals)
* [License](#license)

---

## About the Project

FlowForge is built to support **organization-based multi-tenancy**, enabling teams to manage projects and tasks securely within isolated workspaces.

The system is designed with scalability, security, and real-world backend practices in mind, making it suitable as a **reference architecture** for SaaS-style Django applications.

---

## Key Features

* **Multi-tenant architecture** (Organization-based isolation)
* **Role-based access control**

  * Owner
  * Admin
  * Member
  * Viewer
* **JWT-based authentication**
* CRUD APIs for:

  * Organizations
  * Projects
  * Tasks
* Advanced API capabilities:

  * Filtering
  * Ordering
  * Search
  * Pagination
  * Throttling
* Database-level **query optimization & indexing**
* Clean, modular Django app structure

---

## Tech Stack

* **Backend:** Django, Django REST Framework
* **Authentication:** JWT (Muted)
* **Database:** SQLite3
* **Language:** Python 3.13+
* **DevOps (Planned):**

  * Docker & Docker Compose
  * Jenkins CI/CD
  * Google Cloud Platform (GCP)

---

## Architecture Overview

### Entity Relationship Diagram (ERD)

```
User
 └── <OrganizationMember> ── Organization
        ├── Project
        │     └── Task
        └── Members (roles)
```

### Relationship Summary

* A **User** can belong to multiple **Organizations**
* An **Organization** has many **Projects**
* A **Project** has many **Tasks**
* Tasks can be assigned only to users within the same organization
* Each organization member has a defined role:

  * OWNER / ADMIN / MEMBER / VIEWER

---

## Prerequisites

* Python 3.13+
* PostgreSQL
* `virtualenv` or `venv` (recommended)

---

## Getting Started

### Clone the Repository

```bash
git clone <your-repo-url>
cd flowforge_backend
```

---

### Environment Variables

Create a `.env` file in the project root:

```dotenv
DEBUG=True
SECRET_KEY=your-secret-key

DB_NAME=flowforge
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
```

> ⚠️ Never commit your `.env` file to version control.

---

### Install Dependencies

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

---

### Database Setup & Migrations

```bash
python manage.py migrate
python manage.py createsuperuser
```

---

### Run the Development Server

```bash
python manage.py runserver
```

---

## API Endpoints

Once running locally:

* **API Base:** [http://localhost:8000/api/v1/](http://localhost:8000/api/v1/)
* **Admin Panel:** [http://localhost:8000/admin/](http://localhost:8000/admin/)
* **OpenAPI Schema:** [http://localhost:8000/api/schema/](http://localhost:8000/api/schema/)
* **Swagger UI:** [http://localhost:8000/api/docs/](http://localhost:8000/api/docs/)

---

## Authentication

FlowForge uses **JWT authentication**.

### Obtain Token

```http
POST /api/v1/auth/login/
```

```json
{
  "email": "user@example.com",
  "password": "password"
}
```

### Use Token

```http
Authorization: Bearer <access_token>
```

---

## Query Optimization Notes

This project explicitly addresses common Django performance pitfalls.

### Techniques Used

* `select_related` for foreign-key heavy queries
* `prefetch_related` for reverse relationships
* Database-level indexes on:

  * `(organization, is_active)`
  * `(project, status)`
  * `(assigned_to, status)`
* Pagination enforced on all list endpoints

---

## CI/CD Overview

**(Planned)**

Pipeline stages:

1. Lint & format code
2. Run test suite
3. Build Docker image
4. Push image to registry
5. Deploy to Google Cloud Platform

---

## Deployment (Planned)

* **Cloud Run** – application hosting
* **Cloud SQL** – PostgreSQL
* **Secret Manager** – environment secrets
* **Cloud Logging & Monitoring**

---

## Project Goals

This project is built to demonstrate:

* Clean domain-driven modeling
* Secure multi-tenant backend design
* Scalable database query patterns
* Production-ready Django architecture
* Real-world DevOps workflows

---

## License

This project is licensed under the **MIT License**.
See the [LICENSE](LICENSE) file for details.
