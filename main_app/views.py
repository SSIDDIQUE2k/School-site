# main_app/views.py
from django.shortcuts import render
# Define the home view function
def home(request):
    return render(request, 'home.html')