from django.contrib import admin

from .models import AgendaItem
from .models import SharingItem
from .models import Discuss

# Register your models here.
admin.site.register(AgendaItem)
admin.site.register(SharingItem)
admin.site.register(Discuss)
