from django.shortcuts import render

def load_app(request):
    return render(request, 'index.html', {})