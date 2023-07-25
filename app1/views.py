from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def anusha(request):
    return HttpResponse('<h1>I want to meet you maa</h1>')

def first(request):
    return render(request, 'first.html')

def second(request):
    return render(request, 'second.html')

