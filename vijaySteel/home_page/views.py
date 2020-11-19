from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request, 'home_page.html')

def contact_us(request):
    return render(request, 'contact_us.html')