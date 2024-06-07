from django.contrib import admin
from .models import Note

from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

User = get_user_model()

admin.site.register(User)
admin.site.register(Note)
admin.site.unregister(Group)


