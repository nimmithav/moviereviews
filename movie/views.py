from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html', {'name':'Nimmi'})

def search(request):
    return render(request, 'search.html')



def about(request):
    return HttpResponse('<h1>Welcome to About Page</h1>')

