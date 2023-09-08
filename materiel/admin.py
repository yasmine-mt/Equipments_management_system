from django.contrib import admin
from .models import materiel
from .models import Tag

# Register your models here.
admin.site.register(materiel)
admin.site.register(Tag)