from django.contrib import admin

from .models import AgendaItem
from .models import SharingItem

# Register your models here.
admin.site.register(AgendaItem)
admin.site.register(SharingItem)
