from django.contrib import admin

from .models import *

admin.site.register(Poll)
admin.site.register(Topic)
admin.site.register(Comment)