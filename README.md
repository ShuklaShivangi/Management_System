# Management System

This is a management system built with Django that handles office employee operations, allowing for easy management of employee records through a user-friendly interface.

## Features

- Comprehensive backend using Django for employee data management.
- User-friendly admin interface for seamless management of employee records.
- Supports CRUD (Create, Read, Update, Delete) operations for employee data.
- Efficient handling of user requests to display, add, and filter employee information.

## Setup

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/ShuklaShivangi/Management_System.git
    ```

2. **Navigate to Project Directory:**
    ```bash
    cd Management_System
    ```

3. **Set Up Virtual Environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

4. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5. **Run Migrations:**
    ```bash
    python manage.py migrate
    ```

6. **Create a Superuser (optional):**
    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to create a superuser account for accessing the admin interface.

7. **Start the Development Server:**
    ```bash
    python manage.py runserver
    ```

8. **Open in Browser:**
    Visit `http://127.0.0.1:8000/` to view the application.

## Configuration

- Ensure that your database settings are configured correctly in the `settings.py` file if you are using a different database than the default SQLite.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the Django community for providing a robust framework for web development.
