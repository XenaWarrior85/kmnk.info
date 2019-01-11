from django.shortcuts import render, get_object_or_404
from .models import Person
from .models import Galery

def person(request,id):
    """
    Функция отображения профиля пользователя
    """
    person = get_object_or_404(Person, id=id)
    image = Galery.objects.filter(person_id = id)
    return render(request, 'person.html', {"person":person, "image":image})
