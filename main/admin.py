from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Courses)
admin.site.register(Teachers)
admin.site.register(Subjects)
admin.site.register(Room)
admin.site.register(Lesson)
# admin.site.register(Timetable)