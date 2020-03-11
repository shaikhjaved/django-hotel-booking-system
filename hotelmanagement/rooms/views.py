from django.shortcuts import render, redirect
from .models import Rooms

# Create your views here.


def index(request):
    rooms = Rooms.objects.all()
    context = {'rooms': rooms}
    context['rooms_navlink'] = True
    return render(request, 'rooms/index.html', context)


def onGetCreate(request):
    rooms = Rooms.objects.all()
    room_status = Rooms.ROOM_STATUS
    room_types = Rooms.ROOM_TYPES
    context = {'rooms': rooms, 'room_status': room_status,
               'room_types': room_types}
    context['rooms_navlink'] = True
    return render(request, 'rooms/create.html', context)


def onPostCreate(request):
    if request.method == 'POST':
        room_number = request.POST.get('room_number')
        number_of_beds = request.POST.get('number_of_beds')
        price_per_night = request.POST.get('price_per_night')
        max_person = request.POST.get('max_person')
        room_status = request.POST.get('selectedroomstatus')
        room_type = request.POST.get('selectedroomtypes')

        room = Rooms(room_number=room_number, room_status=room_status, price_per_night=price_per_night,
                     max_person=max_person, number_of_beds=number_of_beds, room_type=room_type)
        room.save()
    return redirect('rooms:index')


def onGetEdit(request, id):
    rooms = Rooms.objects.get(id=id)
    room_status = Rooms.ROOM_STATUS
    room_types = Rooms.ROOM_TYPES
    context = {'rooms': rooms, 'room_status': room_status,
               'room_types': room_types}
    return render(request, 'rooms/edit.html', context)


def onPostEdit(request, id):
    if request.method == 'POST':
        room_number = request.POST.get('room_number')
        number_of_beds = request.POST.get('number_of_beds')
        price_per_night = request.POST.get('price_per_night')
        max_person = request.POST.get('max_person')
        room_status = request.POST.get('selectedroomstatus')
        room_type = request.POST.get('selectedroomtypes')

        Rooms.objects.filter(id=id).update(room_number=room_number, room_status=room_status, price_per_night=price_per_night,
                                           max_person=max_person, number_of_beds=number_of_beds, room_type=room_type)
    return redirect('rooms:index')


def onPostDelete(request, id):
    if request.method == "GET":
        room = Rooms.objects.get(id=id)
        room.delete()
    return redirect('rooms:index')
