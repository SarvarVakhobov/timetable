from django.urls import path
from .views import home, timetable


urlpatterns = [
    path('', home, name='home'),
    path('<str:course_id>/', timetable, name='timetable'),
]
