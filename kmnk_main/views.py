from django.shortcuts import render


__author__ = 'Mikhail Ivanov'  # type: str
__company__ = 'IvanovsCo'



def index(request):
    return render(request, 'main.html', {})