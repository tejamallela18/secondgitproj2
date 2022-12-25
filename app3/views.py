from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def munna(request):
    return  HttpResponse('<h1><marquee><button>bayya la ke bayya MUNNA BHAYYA!!!</button</marquee></h1>')

def compounder(request):
    return HttpResponse('munna bestfriend')
