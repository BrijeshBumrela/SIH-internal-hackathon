from django.contrib import admin
from .models import Room, GenericAsset, Door
# Register your models here.

admin.site.register(Room)
admin.site.register(Door)
admin.site.register(GenericAsset)
