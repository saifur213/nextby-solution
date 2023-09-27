from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')
def contact(request):
    return render(request, 'contact.html')
def company(request):
    return render(request, 'company.html')
def career(request):
    return render(request, 'careers.html')
def privacy(request):
    return render(request, 'privacy.html')