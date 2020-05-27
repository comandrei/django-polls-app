from django.shortcuts import render, get_object_or_404, redirect
from .forms import ClientForm
from .models import Courses, Student, Client
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

def form_client(request, id=None):
    instance = get_object_or_404(Client, pk=id) if id else None
    if request.method == "POST":
        # daca setam la instance ceva diferit de None, formularul va fi bound
        form = ClientForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/school')
    else:
        form = ClientForm(instance=instance)
    context = {'form': form}
    return render(request, 'form_render.html', context)
