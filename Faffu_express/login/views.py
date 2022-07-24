from django.shortcuts import render
from .models import Cliente

# Create your views here.
def login(request):
    cliente = Cliente.objects.all()
    return render(request, "login/login.html", {'cliente' : cliente})