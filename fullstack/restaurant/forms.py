from . import models
from django import forms

class BookingForm(forms.ModelForm):
    """
    A form for creating or updating a booking.

    Inherits from forms.ModelForm and uses the Booking model.

    Available fields: all fields from the Booking model.
    """
    class Meta:
        model = models.Booking
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['first_name'].required and not cleaned_data['first_name']:
            raise forms.ValidationError("First name is required.")
        if cleaned_data['reservation_date'].required and not cleaned_data['reservation_date']:
            raise forms.ValidationError("Select a reservation date.")
        if cleaned_data['reservation_slot'].required and not cleaned_data['reservation_slot']:
            raise forms.ValidationError("Pick a slot.")
        return cleaned_data
    def is_valid(self) -> bool:
        return super().is_valid()
