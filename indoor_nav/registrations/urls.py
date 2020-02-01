from django.urls import path
from . import views

app_name = "registrations"

urlpatterns = [
    path('<str:username>', views.view_user, name="view-user")
]
