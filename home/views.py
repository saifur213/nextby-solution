from django.shortcuts import render
from .models import Package

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