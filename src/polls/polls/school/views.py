from django.shortcuts import render

from .models import Courses
# Create your views here.

def index(request):
    courses = Courses.objects.all()
    context = {
        'nume': 'Test123123',
        'courses': courses,
        'title': 'ana are mere'
    }
    return render(request, 'index.html', context)

