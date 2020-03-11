from django.db import models
from rooms.models import Rooms
from customers.models import Customers
# Create your models here.


class Bookings(models.Model):
    BOOKING_TYPES = (
        (1, 'Guaranteed Reservation'),
        (2, 'Non–Guaranteed Reservation')
    )
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    arrival = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    checkout = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    break_fast = models.IntegerField(blank=True, null=True)
    nights = models.IntegerField(blank=True, null=True)
    comment = models.TextField(max_length=400, blank=True, null=True)
    booking_type = models.PositiveIntegerField(choices=BOOKING_TYPES)
    booking_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    cancelled_at = models.DateTimeField(blank=True, null=True)
    is_cancelled = models.BooleanField(default=False)

    def __str__(self):
        return str(self.booking_type)

    class Meta:
        db_table = "bookings"