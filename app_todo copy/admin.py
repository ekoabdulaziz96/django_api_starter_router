from django.contrib import admin

from .models import Todo as TodoModel
admin.site.register([TodoModel])
