# Riafy Interview Task

## Initial Project Setup
1. Create a virtualenvironment
    ```
    virtualenv -p python3 venv
    ```

2. Activate the virtualenvironment
    ```
    source venv/bin/activate
    ```
3. Install the project dependencies
    ```
    pip install -r requirements.txt
    ```
4. Generate Django Migrations File
    ```
    python manage.py makemigrations
    ```
7. Generate Database Tables from Migrations File
    ```
    python manage.py migrate
    ```
8. Start the development server
    ```
    python manage.py runserver
    ```
