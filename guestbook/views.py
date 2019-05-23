from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'guestbook/index.html')


def add(request):
    name = request.POST['name']
    password = request.POST['password']
    message = request.POST['message']
    return HttpResponse(name + ":" + password + ":" + message)


def deleteform(request):
    return render(request, 'guestbook/deleteform.html')


def delete(request):
    password = request.POST['password']
    return HttpResponse(password)
