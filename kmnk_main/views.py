from django.shortcuts import render
from django.http import HttpResponse

__author__ = 'Mikhail Ivanov'  # type: str
__company__ = 'IvanovsCo'

# { % load staticfiles %}

def index(request):
    return render(request, 'main.html', {})

