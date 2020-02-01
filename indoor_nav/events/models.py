from django.db import models


# Create your models here.
from architecture.models import Room
from registrations.models import Person


class Event(models.Model):
    name = models.CharField(max_length=100)
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    rooms = models.ManyToManyField(to=Room, blank=True)
    incharge = models.ForeignKey(to=Person, on_delete=models.PROTECT)
