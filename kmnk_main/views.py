from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Здесь будет информационный портал посёлка Краснокаменка")
