from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    course = Courses.objects.all()

    context = {
        'course':course,
    }
    return render(request, 'index1.html', context)

def timetable(request, course_id):
    course = Courses.objects.get(course_id=course_id)
    lesson = Lesson.objects.filter(course=course).order_by('para')
    dushanba = lesson.filter(week_day = 'dushanba')
    seshanba = lesson.filter(week_day = 'seshanba')
    chorshanba = lesson.filter(week_day = 'chorshanba')
    payshanba = lesson.filter(week_day = 'payshanba')
    juma = lesson.filter(week_day = 'juma')
    shanba = lesson.filter(week_day = 'shanba')
    context= {
        'dushanba':dushanba,
        'seshanba':seshanba,
        'chorshanba':chorshanba,
        'payshanba':payshanba,
        'juma':juma,
        'shanba':shanba,
    }

    return render(request, 'index.html', context)