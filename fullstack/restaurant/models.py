from django.db import models
from django import forms

class Booking(models.Model):
    """
    Represents a booking made by a user.

    Attributes:
        first_name (str): The first name of the user making the booking.
        reservation_date (date): The date of the reservation.
        reservation_slot (int): The slot number for the reservation.
    """

    first_name = models.CharField(max_length=200, null=False)
    reservation_date = models.DateField(null=False)
    reservation_slot = models.SmallIntegerField(default=10, null=False)

    def __str__(self):
        return self.first_name


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['first_name', 'reservation_date', 'reservation_slot']

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        # Perform sanitization logic here
        # Example: Remove leading/trailing whitespaces
        return first_name.strip()

    def clean_reservation_date(self):
        reservation_date = self.cleaned_data['reservation_date']
        # Perform sanitization logic here
        # Example: Ensure the date is in the future
        return reservation_date

    def clean_reservation_slot(self):
        reservation_slot = self.cleaned_data['reservation_slot']
        # Perform sanitization logic here
        # Example: Ensure the slot is within a valid range
        return reservation_slot

class Menu(models.Model):
    """
    Represents a menu item in a restaurant.
    """

    name = models.CharField(max_length=200)
    price = models.IntegerField(null=False)
    menu_item_description = models.TextField(max_length=1000, default='')

    def __str__(self):
        return self.name
    
    
