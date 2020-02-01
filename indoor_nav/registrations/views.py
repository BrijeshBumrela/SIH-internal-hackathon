from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from architecture.models import Room

def view_user(request, username):
    user = get_object_or_404(User, username=username)
    users = User.objects.all()
    events = user.person.event_set.all()
    room = user.person.room if hasattr(user.person, 'room') else None
    rooms = Room.objects.all()
    context = {'user': user, 'room': room, 'events': events, 'rooms': rooms, "users": users}
    return render(request, "registrations/user_info.html", context)
