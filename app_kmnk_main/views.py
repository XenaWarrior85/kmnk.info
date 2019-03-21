from django.shortcuts import render


__author__ = 'не Ivanov'
__company__ = 'Ivanov@Co'

# каково назначение этого рендера? Можно ли и как обойтись без него?
# не избыточен ли этот код?
def index(request):
    return render(request, 'main.html', {})
