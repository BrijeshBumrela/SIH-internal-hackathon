from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import signals
from django.dispatch import receiver
from rest_framework import validators


def phone_number_validator(phone_number):
    try:
        phone_number = str(phone_number)
    except ValueError:
        raise validators.ValidationError('Invalid Input')

    if phone_number.isdigit() is False:
        raise validators.ValidationError('Phone numbers can only contain numbers')

    if not (10 <= len(phone_number) <= 11):
        raise validators.ValidationError('Length of phone number must be either 10 or 11')


class Person(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    phone_no = models.CharField(verbose_name='Phone Number', max_length=11, null=True, blank=True,
                                validators=[phone_number_validator])
    description = models.TextField(null=True, blank=True)
    profile_photo = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(signals.post_save, sender=User)
def create_profile_and_oauth(sender, instance, created, **kwargs):
    if created:
        Person.objects.create(user=instance)
