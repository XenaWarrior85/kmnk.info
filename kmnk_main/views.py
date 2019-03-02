from django.shortcuts import render


__author__ = 'Mikhail Ivanov'  # type: str
__company__ = 'Ivanov@Co'



def index(request):
    return render(request, 'main.html', {})