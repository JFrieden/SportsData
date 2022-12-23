from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, me, you've reached the index of your app")

def test(request):
    return HttpResponse("Sup b")