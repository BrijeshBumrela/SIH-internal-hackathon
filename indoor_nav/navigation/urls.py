from django.urls import path
from . import views

app_name = "navigation"

urlpatterns = [
    path('', views.empty_navigate, name="empty-navigate"),
    path('<str:source>/<str:dest>', views.navigate, name="full-navigate"),
    path('<str:dest>', views.dest_navigate, name="dest-navigate"),
]
