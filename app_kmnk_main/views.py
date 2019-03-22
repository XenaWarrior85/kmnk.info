from django.shortcuts import render


__author__ = 'не Ivanov'
__company__ = 'Ivanov@Co'

# функция старта проекта Краснокаменка (индекс)
# вызывается с главной страницы, загружает шаблон главной страницы
def index(request):
    return render(request, 'main.html', {})
