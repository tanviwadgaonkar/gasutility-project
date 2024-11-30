# Gas Utility Service Management System

## Overview
This Django-based application provides a platform for managing consumer services for a gas utility company. It allows customers to submit service requests, track the status of their requests, and view their account information. Customer support representatives can also manage requests and provide support efficiently.

## Features

### Customer Features
- **Service Requests:**
  - Submit requests online with details and file attachments.
  - View and manage submitted requests.
- **Request Tracking:**
  - Monitor the status of service requests.
  - View submission and resolution dates.
- **Account Information:**
  - Access personal account details, including address and contact information.

### Support Features
- **Request Management:**
  - View and update the status of all service requests.
  - Ensure timely resolution with administrative tools.
- **User Management:**
  - Manage customer accounts and user data.

## Application Structure
```
gas_utility_system/
├── gas_utility_system/  # Main project directory
│   ├── settings.py      # Project settings
│   ├── urls.py          # URL configurations
│   ├── wsgi.py          # WSGI configuration
│   ├── asgi.py          # ASGI configuration
│   └── __init__.py
├── customer_service/    # Main app for customer service management
│   ├── models.py        # Database models
│   ├── views.py         # Core business logic
│   ├── forms.py         # Forms for user input
│   ├── admin.py         # Admin interface configuration
│   ├── urls.py          # App-specific URL routing
│   ├── templates/       # HTML templates
│   ├── static/          # Static files (CSS, JS, Images)
│   └── migrations/      # Database migration files
├── manage.py            # Django management tool
└── README.md            # Project documentation
```

## Installation
1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd gas_utility_system
   ```
2. **Set Up a Virtual Environment:**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Set Up the Database:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```
6. **Access the Application:**
   Open `http://127.0.0.1:8000` in your browser.

## Usage
### For Customers
- Sign up or log in to submit and track service requests.
- Use the dashboard to view account information and service request history.

### For Admins/Support Staff
- Log in to the admin interface (`/admin`) to manage user accounts and requests.
- Update request statuses and ensure timely resolution.

## Contributing
We welcome contributions to improve this application. Please follow these steps:
1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Submit a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact
For any inquiries or support, please contact us at support@gasutilitycompany.com.


[Watch the video](video1851612785.mp4)
After clicking on watch the video download the video to watch it
