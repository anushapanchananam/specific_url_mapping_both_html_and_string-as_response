from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def three(request):
    return render(request, 'three.html')
def four(request):
    return render(request, 'four.html')
def vyshu(request):
    return HttpResponse('<h1>All the best</h1>')