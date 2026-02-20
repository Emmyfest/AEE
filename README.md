# Agricultural & Environmental Engineering Department Portal

A comprehensive Flask-based web application for the Agricultural & Environmental Engineering Department at the University of Ibadan. This system manages student payments, academic results, and departmental operations.

## Features

### Public Features
- **Homepage**: Modern responsive landing page with department information
- **Payment Portal**: Secure payment submission system with receipt upload
- **Staff Directory**: Faculty and staff information
- **News & Updates**: Department announcements and events

### Student Portal
- **Dashboard**: View academic results and CGPA
- **Payment Management**: Submit and track departmental payments
- **Result Access**: View semester results (requires approved payment)
- **Print/Download Results**: Generate PDF reports of academic records

### Admin Portal
- **Dashboard**: Overview of departmental statistics
- **Student Management**: View and manage student accounts
- **Payment Approval**: Review and approve/reject payment submissions
- **Result Upload**: Upload student results with course autocomplete
- **Data Export**: Export contacts and payments to CSV
- **Statistics**: View payment trends and analytics

## Technology Stack

- **Backend**: Flask 3.0.3
- **Database**: PostgreSQL (via psycopg 3.1.10)
- **Email**: Flask-Mail
- **Server**: Gunicorn
- **Frontend**: Bootstrap 5.3, Font Awesome 6.4, Vanilla JavaScript

## Installation

### Prerequisites
- Python 3.11+
- PostgreSQL database
- SMTP server (for email notifications)

### Local Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd aee-portal
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set environment variables**
   Create a `.env` file or set the following:
   ```
   DATABASE_URL=postgresql://username:password@host:port/database_name
   SESSION_SECRET=your-secret-key-here
   MAIL_SERVER=smtp.gmail.com
   MAIL_PORT=587
   MAIL_USERNAME=your-email@gmail.com
   MAIL_PASSWORD=your-email-password
   MAIL_DEFAULT_SENDER=your-email@gmail.com
   ```

4. **Initialize the database**
   The application will automatically create tables and seed default data on first run:
   ```bash
   python main.py
   ```

5. **Access the application**
   - Homepage: http://localhost:5000
   - Admin Login: http://localhost:5000/admin/login
   - Student Login: http://localhost:5000/student/login

### Default Credentials

**Admin Account:**
- Username: `admin`
- Password: `ChangeMeOnFirstLogin2024!` (or set via `INITIAL_ADMIN_PASSWORD` environment variable)

**CRITICAL SECURITY NOTE**: 
- You MUST change the default admin password immediately after first login!
- For production deployments, set `INITIAL_ADMIN_PASSWORD` environment variable to a strong password before first deployment
- The default admin is only created if no admin accounts exist in the database

## Deployment to Render

1. **Create a Render account** at https://render.com

2. **Create a PostgreSQL database**
   - Go to "New +" → "PostgreSQL"
   - Name: `aee-database`
   - Note the "External Database URL" provided

3. **Create a Web Service**
   - Go to "New +" → "Web Service"
   - Connect your Git repository
   - Settings:
     - Name: `aee-portal`
     - Environment: `Python 3`
     - Build Command: `pip install -r requirements.txt`
     - Start Command: `gunicorn main:app --bind 0.0.0.0:$PORT --workers 2`

4. **Add Environment Variables**
   In the Render dashboard, add:
   - `DATABASE_URL`: Your PostgreSQL External Database URL
   - `SESSION_SECRET`: Generate a random string (or let Render auto-generate)
   - `MAIL_SERVER`: Your SMTP server
   - `MAIL_PORT`: SMTP port (usually 587)
   - `MAIL_USERNAME`: Your email
   - `MAIL_PASSWORD`: Your email password
   - `MAIL_DEFAULT_SENDER`: Your email

5. **Deploy**
   - Click "Create Web Service"
   - Wait for deployment to complete
   - Access your live application!

Alternatively, use the included `render.yaml` for automatic configuration.

## Project Structure

```
.
├── main.py                 # Application entry point
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── Procfile               # Process configuration
├── render.yaml            # Render deployment config
├── static/
│   ├── css/
│   │   └── style.css      # Custom styles
│   ├── js/
│   │   └── main.js        # Custom JavaScript
│   └── images/            # Department images
├── templates/
│   ├── admin/             # Admin panel templates
│   ├── base.html          # Base template
│   ├── index.html         # Homepage
│   ├── student_dashboard.html
│   ├── login.html
│   └── register.html
└── uploads/
    └── receipts/          # Payment receipt uploads
```

## Database Schema

### Tables

1. **students** - Student information and credentials
2. **admins** - Admin users and roles
3. **payments** - Payment submissions and status
4. **results** - Student academic results
5. **courses** - Course catalog
6. **sessions** - Academic sessions
7. **contacts** - Contact form submissions

## Security Features

- **Separate Authentication**: Admin and student sessions are completely isolated
- **Password Hashing**: All passwords are hashed using Werkzeug security
- **Payment Verification**: Students must have approved payment to access results
- **CSRF Protection**: Built-in Flask session protection
- **Secure File Uploads**: File type and size validation for receipts

## Payment Flow

1. Student submits payment through the portal
2. Uploads payment receipt (PDF, JPG, PNG)
3. Admin reviews payment in admin panel
4. Admin approves/rejects payment
5. Once approved, student can access academic results

## Admin Functions

- View all students and their status
- Approve/reject student registrations
- Review and approve payments
- Upload student results with course autocomplete
- Export data to CSV
- View departmental statistics

## Support

For issues or questions:
- Contact: Department of Agricultural & Environmental Engineering
- Email: [department-email]
- Phone: [department-phone]

## License

© 2024 University of Ibadan - Agricultural & Environmental Engineering Department
