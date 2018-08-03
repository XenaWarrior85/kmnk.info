from django.shortcuts import render
from django.http import HttpResponse

__author__ = 'Mikhail Ivanov'  # type: str
__company__ = 'IvanovsCo'

# { % load staticfiles %}
def index(request):
    return HttpResponse("""Здесь будет информационный портал посёлка Краснокаменка.<p><p>
    Цель проекта: информационное обеспечение самоуправления и развития экономики посёлка.<p>
    Через сайт каждый житель посёлка сможет предложить свои услуги, задать вопросы, принять участие во всех делах и жизни посёлка. <P> 
    Организатор: <p><p>
    <img src="static/я.jpg" alt="Михаил Леонидович Иванов" width="150" /><p><p>
    Михаил Леонидович Иванов, +7-978-934-87-07<p>
                        """)

