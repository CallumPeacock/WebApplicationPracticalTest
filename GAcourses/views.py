from django.shortcuts import render
from django.http import HttpResponse
from GAcourses.models import Course
# Create your views here.

def course(request):
    course_list = Course.objects.all()
    context_dict = {}
    context_dict['courses'] = course_list
    # Render the response and send it back!
    return render(request, 'GACourses/course.html', context=context_dict)