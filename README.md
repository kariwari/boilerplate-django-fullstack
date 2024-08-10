# Django Fullstack Boilerplate

This project is a fullstack boilerplate built with Django, designed to accelerate web application development with pre-built basic functionalities.

> **Note:** You can use this boilerplate by simply clicking the "Use this template" button at the top right of this repository.

## Features

This boilerplate comes with essential user management features (users app), including:

- Login
- Register
- Reset Password
- Change Password
- Email Verification
- Profile Update

## Requirements

- Python 3.8+
- pip

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/kariwari/boilerplate-django-fullstack.git
    cd boilerplate-django-fullstack
    ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # For Unix or MacOS
    venv\Scripts\activate  # For Windows
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the project root and fill it with the necessary configuration *(copy from `.env.example`)*:

5. Run migrations:

    ```bash
    python manage.py migrate
    ```

6. Create a superuser (optional):

    ```bash
    python manage.py createsuperuser
    ```

7. To run the development server:

    ```bash
    python manage.py runserver
    ```

Access the application in your browser at `http://localhost:8000`.

## Customization

- Add new apps by running `python manage.py startapp app_name`
- Modify templates in the `templates/` folder
- Add static files in the `static/` folder

## Contributing

Contributions are always welcome. Please open an issue or submit a pull request for any improvements or additional features.

## License

[MIT License](LICENSE)