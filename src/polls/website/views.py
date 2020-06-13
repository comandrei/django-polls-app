from django.shortcuts import render
from .forms import ContactForm

def contact(request):
    ctx = {}
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            ctx['thank_you'] = form.cleaned_data['message']
    else:
        form = ContactForm()
    ctx['form'] = form
    return render(request, 'contact.html', context=ctx)

def load_app(request):
    return render(request, 'index.html', {})