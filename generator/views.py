from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'home.html')


def password(request):
    characters = list('abcdefghijkalmnopqrstuvwxyz')
    
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    if request.GET.get('special'):
        characters.extend(list('@!#$%&*'))

    length = int(request.GET['length'])
    thepassword = ""
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'password.html',{'password':thepassword})