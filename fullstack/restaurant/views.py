from django.http import HttpResponse
from django.shortcuts import render
from .models import Menu
from django.core import serializers
from .models import Booking
from django.utils import timezone
import json
from .forms import BookingForm
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
from django.utils import timezone


def home(request):
    """
    Renders the home page.

    Args:
        request: The HTTP request object.

    Returns:
        The rendered index.html template.
    """
    return render(request, 'index.html')


def about(request):
    """
    Renders the about.html template.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - The rendered about.html template.
    """
    return render(request, 'about.html')


def book(request):
    """
    View function for booking a table.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.

    """
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'book.html', context)


def reservations(request):
    """
    View function for handling reservations.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the rendered bookings.html template.
    """
    date = request.GET.get(
        'date', timezone.now().date().strftime('%YYYY-%MM-%dd'))
    bookings = Booking.objects.all()
    booking_json = serializers.serialize('json', bookings)
    return render(request, 'bookings.html', {"bookings": booking_json})


def bookings(request):
    """
    View function for displaying bookings.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - A rendered HTML template with the bookings data.
    """
    date = request.GET.get(
        'date', timezone.now().date().strftime('%YYYY-%MM-%dd'))
    bookings = Booking.objects.all()
    booking_json = serializers.serialize('json', bookings)
    return render(request, 'bookings.html', {'bookings': booking_json})


def menu(request):
    """
    Renders the menu page with the menu data.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered menu page.
    """
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})


def display_menu_item(request, pk=None):
    """
    Display a menu item based on the given primary key (pk).

    Args:
        request (HttpRequest): The HTTP request object.
        pk (int, optional): The primary key of the menu item. Defaults to None.

    Returns:
        HttpResponse: The rendered HTML template with the menu item data.
    """
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ""
    return render(request, 'menu_item.html', {"menu_item": menu_item})


@csrf_exempt
def bookings(request):
    """
    View function for handling bookings.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing booking information in JSON format.
    """
    if request.method == 'POST':
        data = json.load(request)
        exist = Booking.objects.filter(reservation_date=data['reservation_date']).filter(
            reservation_slot=data['reservation_slot']).exists()
        if not exist:
            booking = Booking(
                first_name=data['first_name'],
                reservation_date=data['reservation_date'],
                reservation_slot=data['reservation_slot']
            )
            print(booking)
            booking.save()
        else:
            return HttpResponse("{'error':1}", content_type='application/json')
    date = str(request.GET.get('date', timezone.now().date().strftime('%YYYY-%MM-%dd')))
    print('DATE:', date)
    try:
        bookings = Booking.objects.all().filter(reservation_date=date)
        booking_json = serializers.serialize('json', bookings)
    except ValidationError as e:
        print('ValidationError', e)
        booking_json = serializers.serialize('json', [])
    return HttpResponse(booking_json, content_type='application/json')
