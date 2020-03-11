from django.shortcuts import render, redirect
from django.db.models import Q
from bookings.models import Bookings
from rooms.models import Rooms
# Create your views here.


def index(request):
    available_rooms = Rooms.objects.filter(
        Q(bookings__isnull=True) | Q(bookings__is_cancelled=True)).values()

    all_bookings = Bookings.objects.filter(checkout__isnull=True)

    context = {'available_rooms': available_rooms,
               'all_bookings': all_bookings}

    context['home'] = True

    return render(request, 'index.html', context)
