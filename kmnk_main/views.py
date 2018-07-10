__author__ = 'Mikhail Ivanov'  # type: str
__company__ = 'IvanovsCo'

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Здесь будет информационный портал посёлка Краснокаменка")
