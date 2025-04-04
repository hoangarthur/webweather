from django.shortcuts import render
from .form import RegistrationForm
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    return render(request, 'pages/home.html')
def home(request):
    return render(request, 'pages/home.html')
def contact(request):
    return render(request, 'pages/contact.html')
def error(request, exception):
    # Your error handling code here
    return render(request, 'pages/error.html')
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'pages/register.html', {'form': form})
