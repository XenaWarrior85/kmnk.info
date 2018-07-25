from django.shortcuts import render
from django.http import HttpResponse

__author__ = 'Mikhail Ivanov'  # type: str
__company__ = 'IvanovsCo'

# { % load staticfiles %}
def index(request):
    return HttpResponse("""Здесь будет информационный портал посёлка Краснокаменка.<p><p>
    Цель проекта: информационное обеспечение самоуправления и развития экономики посёлка.<p>
    Организатор: Михаил Иванов, +7-978-934-87-07<p>
    <img src="static/я.jpg" alt="Михаил Иванов"/>
                        """)

