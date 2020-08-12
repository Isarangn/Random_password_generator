from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'home.html')


def password(request):
    charactors = list('abcdefghijkalmnopqrstuvwxyz')
    length = 10
    thepassword = ""
    for x in range(length):
        thepassword += random.choice(charactors)

    return render(request, 'password.html',{'password':thepassword})