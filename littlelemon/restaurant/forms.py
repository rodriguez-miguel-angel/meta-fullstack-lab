from django.forms import ModelForm
from .models import Booking


# Code added for loading form data on the Booking page
class BookingForm(ModelForm):
    class Meta:
        model = Booking
        """
        version-01:
        fields = "__all__"

        version-02:
        """
        fields = ('id','first_name', 'reservation_date', 'reservation_slot')
