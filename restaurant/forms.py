from django.forms import ModelForm
from .models import BookingTable


# Code added for loading form data on the Booking page
class BookingForm(ModelForm):
    class Meta:
        model = BookingTable
        fields = "__all__"
