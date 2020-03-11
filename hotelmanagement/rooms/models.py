from django.db import models

# Create your models here.


class Rooms(models.Model):
    ROOM_TYPES = (
        (1, 'Single'),
        (2, 'Double'),
        (3, 'Triple'),
    )

    ROOM_STATUS = (
        (1, 'OCCUPIED'),
        (2, 'STAYOVER'),
        (3, 'ON-CHANGE'),
        (4, 'DO-NOT-DISTURB'),
        (5, 'CLEANING-IN-PROGRESS'),
        (6, 'SLEEP-OUT'),
        (7, 'ON-QUEUE'),
        (8, 'SKIPPER'),
        (9, 'VACANT-AND-READY'),
        (10, 'OUT-OF-ORDER'),
        (11, 'OUT-OF-SERVICE'),
        (12, 'LOCK-OUT'),
        (13, 'DID-NOT-CHECK-OUT)'),
        (14, 'DUE-OUT'),
        (15, 'CHECK-OUT'),
        (16, 'LATE-CHECK-OUT'),
    )

    room_number = models.IntegerField(blank=True, null=True)
    room_type = models.PositiveIntegerField(choices=ROOM_TYPES)
    price_per_night = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    max_person = models.IntegerField(blank=True, null=True)
    room_status = models.PositiveIntegerField(choices=ROOM_STATUS)
    number_of_beds = models.IntegerField(blank=True, null=True)
    locked = models.CharField(max_length=50)
    created_date = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
        
    class Meta:
        db_table = "rooms"