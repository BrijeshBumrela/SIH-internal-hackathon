from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from .models import Room


# Create your views here.
def view_room(request, room_number):
    room = Room.objects.filter(ga__number=room_number).first()
    rooms = Room.objects.all()

    user = room.occupant.user if hasattr(room.occupant, "user") else None
    events = room.event_set.all() if hasattr(room, "event_set") else []
    users = User.objects.all()
    context = {'room': room, 'user': user, 'events': events, 'rooms': rooms, 'users': users}
    return render(request, "architecture/view_room.html", context)
