from django.shortcuts import render, get_object_or_404

from .models import Courses, Student
# Create your views here.

def index(request):
    courses = Courses.objects.all()
    request.session['views'] = request.session.get('views', 0) + 1
    context = {
        'nume': 'Test123123',
        'courses': courses,
        'title': 'ana are mere'
    }
    return render(request, 'index.html', context)

def list_student(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'students.html', context)

def carnet_note(request, cucu_student_id):
    student = get_object_or_404(Student, pk=cucu_student_id)
    context= {
        "student": student,
    }
    return render(request, 'carnet_note.html', context)

