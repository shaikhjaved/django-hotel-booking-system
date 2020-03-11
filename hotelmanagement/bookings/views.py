from django.shortcuts import render, redirect
from .models import Bookings
from rooms.models import Rooms
from customers.models import Customers
from django.http import HttpResponse, JsonResponse
import datetime
import json
from django.core import serializers

# Create your views here.


def index(request):
    bookings = Bookings.objects.all()
    booking_types = Bookings.BOOKING_TYPES

    q1 = Rooms.objects.filter(bookings__isnull=True).values()
    q2 = Rooms.objects.filter(bookings__is_cancelled=True).values()

    available_rooms = q1.union(q2)

    rooms = Rooms.objects.all()
    room_types = Rooms.ROOM_TYPES
    customers = Customers.objects.all()

    context = {'bookings': bookings, 'booking_types': booking_types,
               'rooms': available_rooms, 'room_types': room_types, 'customers': customers}
    context['bookings_navlink'] = True
    return render(request, 'bookings/index.html', context)


def onGetCreate(request):
    pass


def onPostCreate(request):
    if request.method == 'POST':
        customer = request.POST.get('selectedcustomer')
        booking_types = request.POST.get('selectedbookingtypes')
        room_number = request.POST.get('selectedroom')
        arrival_datetime = request.POST.get('arrival_datetime')
        comments = request.POST.get('comments')
        booking = Bookings(customer_id=customer, booking_type=booking_types,
                           room_id=room_number, arrival=arrival_datetime, comment=comments)
        booking.save()
    return redirect('bookings:index')


def onGetEdit(request, id):
    allbookings = Bookings.objects.all().values()
    bookings = Bookings.objects.get(id=id)
    booking_types = Bookings.BOOKING_TYPES

    rooms = Rooms.objects.all()
    room_types = Rooms.ROOM_TYPES
    customers = Customers.objects.all()

    context = {'bookings': bookings, 'booking_types': booking_types,
               'rooms': rooms, 'room_types': room_types, 'customers': customers, 'allbookings': allbookings}
    return render(request, 'bookings/edit.html', context)


def onPostEdit(request, id):
    if request.method == 'POST':
        customer = request.POST.get('selectedcustomer')
        booking_types = request.POST.get('selectedbookingtypes')
        room_number = request.POST.get('selectedroom')
        arrival_datetime = request.POST.get('arrival_datetime')
        comments = request.POST.get('comments')

        Bookings.objects.filter(id=id).update(customer_id=customer, booking_type=booking_types,
                                              room_id=room_number, arrival=arrival_datetime, comment=comments)
    return redirect('bookings:index')


def onPostCancel(request):
    hidden_booking_id = request.POST.get('hidden_booking_id')
    Bookings.objects.filter(id=hidden_booking_id).update(is_cancelled=True)
    return redirect('bookings:index')

def OnGetCheckout(request, booking_id):
    bookings = Bookings.objects.filter(id=booking_id)
    bookings_dict = {}
    for target_list in bookings:
        bookings_dict["room_number"] = target_list.room.room_number
        bookings_dict["customer_name"] = target_list.customer.first_name +' '+ target_list.customer.last_name
        start_date = datetime.datetime.strptime(str(target_list.arrival)[:16], "%Y-%m-%d %H:%M")
        end_date = datetime.datetime.strptime(str(datetime.datetime.now())[:16], "%Y-%m-%d %H:%M")
        diff = abs((end_date-start_date).days)
        bookings_dict["total_amount"] = float(diff) * float(target_list.room.price_per_night)

    return HttpResponse(json.dumps(bookings_dict), content_type="application/json")

def OnPostCheckout(request):
    hidden_booking_id = request.POST.get('hidden_booking_id')
    Bookings.objects.filter(id=hidden_booking_id).update(checkout=datetime.datetime.now())
    return redirect('home:index')

def onPostDelete(request):
    pass