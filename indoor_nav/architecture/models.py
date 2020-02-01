from django.db import models
from registrations.models import Person


# Create your models here.
class GenericAsset(models.Model):
    FLOOR_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3')
    )
    number = models.CharField(max_length=10)
    name = models.CharField(max_length=100, null=True, blank=True)
    floor = models.IntegerField(choices=FLOOR_CHOICES)
    fig_id = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name if self.name else self.number


class Room(models.Model):
    ROOM_TYPE_CHOICES = (
        ('office', 'Office'),
        ('faculty_cabin', 'Faculty Cabin'),
        ('classroom', 'Class Room'),
        ('lab', 'Lab'),
        ('workspace', 'Workspace'),
        ('other', 'Other')
    )

    ga = models.OneToOneField(to=GenericAsset, on_delete=models.CASCADE)
    room_type = models.CharField(max_length=100, choices=ROOM_TYPE_CHOICES)
    occupant = models.OneToOneField(to=Person, null=True, blank=True, on_delete=models.CASCADE)

    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.ga.name if self.ga else "Room"


class Door(models.Model):
    ga = models.OneToOneField(to=GenericAsset, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
