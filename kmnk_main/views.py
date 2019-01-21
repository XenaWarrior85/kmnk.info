from django.shortcuts import render
from django.contrib.auth.decorators import login_required

__author__ = 'Mikhail Ivanov'  # type: str
__company__ = 'IvanovsCo'


@login_required(login_url='/login')
def index(request):
    return render(request, 'main.html', {})


def authapp_sign_up(request):
    return render(request, 'sign_up.html', {})