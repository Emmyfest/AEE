# Overview

This is a comprehensive web application for the Agricultural & Environmental Engineering Department at the University of Ibadan. The system manages student registration, departmental payments with receipt verification, academic results, and administrative operations. Built with Flask and PostgreSQL, it features fully separated authentication systems for students and administrators, payment approval workflows, result management, and data export capabilities.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Backend Framework
- **Flask 3.0.3**: Web framework handling routing, templating, and request processing
- **Gunicorn**: Production WSGI server for deployment on Render.com
- **Session Management**: Server-side sessions with separate session keys for students (`STUDENT_SESSION_KEY`) and admins (`ADMIN_SESSION_KEY`) to prevent cross-contamination

## Database Architecture
- **PostgreSQL**: Primary database using psycopg 3.1.10 with connection pooling
- **Pure psycopg3 Implementation**: Direct database operations without ORM
- **Database Schema**:
  - `students`: Student records with authentication credentials, activation status
  - `admins`: Admin users with role-based access (super_admin, exam_officer, hod)
  - `payments`: Payment submissions with approval status and receipt storage
  - `results`: Academic results linked to students and courses
  - `courses`: Course catalog with codes, titles, and credit units
  - `sessions`: Academic session management
  - `contacts`: Contact form submissions from public website
- **Foreign Key Relationships**: Enforced constraints between students, payments, and results
- **Indexing**: Performance optimization on frequently queried fields

## Authentication System
- **Dual Authentication**: Completely separated authentication flows for students and administrators
- **Password Security**: Werkzeug security for password hashing
- **Decorators**: `@student_login_required` and `@admin_login_required` for route protection
- **Role-Based Access Control**: Admin roles determine access to specific administrative functions
- **Account Management**: Admin-controlled student account activation/deactivation

## Payment Processing
- **Payment Submission**: Students submit payment details with receipt uploads
- **Approval Workflow**: Three-state system (pending, approved, rejected)
- **Access Control**: Students cannot view results until payment is approved
- **File Uploads**: Secure filename handling for receipt images
- **Statistics**: Payment tracking by level, session, and status

## Result Management
- **Course Autocomplete**: Dynamic course selection for result uploads
- **CGPA Calculation**: Automated grade point average computation
- **PDF Generation**: Result reports with print/download functionality
- **Access Gating**: Results only visible to students with approved payments

## Email System
- **Flask-Mail**: Email notifications for payment approvals and other communications
- **SMTP Configuration**: Environment-based mail server configuration

## Frontend Architecture
- **Bootstrap 5.3**: Responsive UI framework
- **Font Awesome 6.4**: Icon library
- **Custom CSS**: Department branding with CSS variables for theming
- **Vanilla JavaScript**: Client-side interactions without heavy frameworks
- **Template Engine**: Jinja2 for server-side rendering

## File Structure
- **Separation of Concerns**: Templates organized by user type (admin/, student/, public)
- **Static Assets**: CSS, JavaScript, and images organized by purpose
- **Environment Configuration**: Secrets managed via environment variables

## Security Measures
- **Session Security**: HTTP-only, SameSite cookies
- **CSRF Protection**: Implicit through session management
- **SQL Injection Prevention**: Parameterized queries throughout
- **Secure File Uploads**: Filename sanitization with werkzeug.utils.secure_filename
- **Environment Secrets**: DATABASE_URL and SESSION_SECRET required from environment

## Data Export
- **CSV Export**: Contact and payment data exportable for reporting
- **Statistics Dashboard**: Payment analytics by level and session

# External Dependencies

## Database
- **PostgreSQL**: Required external database service
- **Connection String**: Must be provided via `DATABASE_URL` environment variable
- **Format**: `postgresql://username:password@host:port/database_name`
- **Deployment**: Configured for Render.com PostgreSQL service

## SMTP Email Service
- **Flask-Mail Configuration**: Requires external SMTP server
- **Environment Variables**: MAIL_SERVER, MAIL_PORT, MAIL_USERNAME, MAIL_PASSWORD, MAIL_USE_TLS/SSL
- **Purpose**: Payment approval notifications and contact form responses

## Python Dependencies
- **Flask**: 3.0.3 (web framework)
- **Flask-Mail**: 0.9.1 (email handling)
- **Werkzeug**: 3.0.3 (security utilities)
- **psycopg**: 3.1.10 with binary drivers (PostgreSQL adapter)
- **gunicorn**: 23.0.0 (production server)

## Frontend CDN Resources
- **Bootstrap**: 5.3.0 from cdn.jsdelivr.net
- **Font Awesome**: 6.4.0 from cdnjs.cloudflare.com
- **Google Fonts**: Playfair Display and Inter fonts

## Deployment Platform
- **Render.com**: Primary deployment target
- **Configuration Files**: render.yaml, Procfile, requirements.txt, runtime.txt
- **Python Runtime**: 3.11.10

## File Storage
- **Local Storage**: Receipt uploads stored in filesystem (deployment may require persistent volume or S3 integration)
- **Static Files**: Served directly by Flask in development, should use CDN/object storage in production