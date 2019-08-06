from django.contrib import admin
# to let superuser see this app
# Register your models here.
from .models import Job

admin.site.register(Job)
