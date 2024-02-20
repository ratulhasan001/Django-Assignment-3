from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'index.html')
def contact(request):
    return render(request, 'firstapp/contact.html')
def about(request):
    return render(request, 'firstapp/about.html')