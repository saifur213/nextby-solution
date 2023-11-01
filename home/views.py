from django.shortcuts import render
from .models import Package, Contact, CustomUser

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    package = Package.objects.all()
    return render(request, 'index.html', {'pck':package})
def contact(request):
    return render(request, 'contact.html')
def company(request):
    return render(request, 'company.html')
def career(request):
    return render(request, 'careers.html')
def privacy(request):
    return render(request, 'privacy.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        user = CustomUser(username=username, first_name=firstname, last_name=lastname, email=email, password1=password1, password2=password2)
        user.save()
        return render(request, 'index.html')  # Redirect to a success page
    return render(request, 'index.html')

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('phone')
        message = request.POST.get('message')

        contact = Contact(name=name, email=email, mobile=mobile, message=message)
        contact.save()
        return render(request, 'contact.html')  # Redirect to a success page
    return render(request, 'contact.html')