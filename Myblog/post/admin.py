from django.contrib import admin
from .models import MyPost

from django.contrib.auth.models import Group

admin.site.register(MyPost)
admin.site.unregister(Group)
# Register your models here.
