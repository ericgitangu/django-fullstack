# Little Lemon Restaurant

This is a Django project for the Little Lemon Restaurant website.

## Project Description

The Little Lemon Restaurant website is built using Django for the back-end, MySQL as the database, and JavaScript for handling form components of the template. HTML with supportive stylesheets are already added as part of the starter code.

## Project Structure

The project directory is named `littlelemon` and the app is named `restaurant`.

## Getting Started

To get started with the project, follow these steps:

1. Install `pipenv` if you haven't already.
2. Create a virtual environment using `pipenv`.
3. Activate the virtual environment.
4. Install the project dependencies using `pipenv`.
5. Set up the MySQL database and configure the Django settings accordingly.
6. Run the Django development server.

## Project: littlemon

## Apps: restaurant

### Models

1. Menu
2. Booking

### Views

1. def home(request)

    """
    Renders the home page.

    Args:
        request: The HTTP request object.

    Returns:
        The rendered index.html template.
    """

2. def about(request):
    """
    Renders the about.html template.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - The rendered about.html template.
    """

3. def book(request):
    """
    View function for booking a table.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.

    """

4. def reservations(request):
    """
    View function for handling reservations.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the rendered bookings.html template.
    """

5. def bookings(request):
    """
    View function for displaying bookings.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - A rendered HTML template with the bookings data.
    """

6. def menu(request):
    """
    Renders the menu page with the menu data.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered menu page.
    """

7. def display_menu_item(request, pk=None):
    """
    Display a menu item based on the given primary key (pk).

    Args:
        request (HttpRequest): The HTTP request object.
        pk (int, optional): The primary key of the menu item. Defaults to None.

    Returns:
        HttpResponse: The rendered HTML template with the menu item data.
    """

8. def bookings(request):
    """
    View function for handling bookings.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing booking information in JSON format.
    """

### Forms

1. Booking Form, inheriting from the ModelForm it uses as it Model the Booking Model and does some client-side validations and set up the necessary Form DB attibutes

## Running locally

1. cd littlelemon

2. pipenv shell

3. pipenv install

4. python manage.py makemigrations

5. python manage.py migrate

6. python manage.py runserver

## Requirement

1. MySQL Instance
2. Django-specific requirements can be found in the requirements.txt file.
