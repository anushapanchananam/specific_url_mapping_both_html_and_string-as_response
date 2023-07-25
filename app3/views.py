from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def five(request):
    return render(request, 'five.html')
def six(request):
    return render(request, 'six.html')
def saila(request):
    return HttpResponse('<h1>All the best</h1>')