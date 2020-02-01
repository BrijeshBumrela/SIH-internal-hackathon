from django.urls import path
from . import views

app_name = "architecture"

urlpatterns = [
    path('<str:room_number>', views.view_room, name="view-room"),
]
