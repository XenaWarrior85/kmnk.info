from django.shortcuts import render, get_object_or_404
from .models import Person
from .models import Galery
from .forms import UserForm, ImageForm, PersonForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from  django.contrib.auth import authenticate, login


def person(request, id):
    """
    Функция отображения профиля пользователя
    """
    person = get_object_or_404(Person, id=id)
    image = Galery.objects.filter(person_id=id)

    return render(request, 'person.html',
                  {"person": person,
                   "image": image,
                   })


def add_person(request, id):
    """
      Функция добавления профиля пользователя
    """
    user_form = UserForm()
    image_form = ImageForm()
    person_form = PersonForm()

    if request.method == "POST":

        user_form = UserForm(request.POST)
        person_form = PersonForm(request.POST)
        image_form = ImageForm(request.POST, request.FILES)

        if user_form.is_valid() and image_form.is_valid() and person_form.is_valid():

            last_id = Person.objects.latest('id').id
            new_user = User.objects.create_user(**user_form.cleaned_data, id=int(last_id)+1)
            new_person = person_form.save(commit=False,)
            new_person.users = new_user
            new_person.save()
            new_image = image_form.save(commit=False)
            new_image.person_id = last_id+1
            new_image.users = new_user
            new_image.save()

            user = authenticate(
                username=user_form.cleaned_data['username'],
                password=user_form.cleaned_data['password']
            )
            login(request, user)

            return HttpResponseRedirect('{}?sent=True'.format(reverse('add_person', kwargs={'id': id})))

    return render(request, 'person_add.html',
                  {"user_form": user_form,
                   "id": id,
                    "image_form": image_form,
                    "person_form": person_form,
                    'sent': request.GET.get('sent', False)})


def edit_person(request, id):
    """
      Функция редактирования профиля пользователя
    """
    users_id = Person.objects.get(id=id).users_id
    user_form = UserForm(instance=User.objects.get(id=int(users_id)))
    image_form = ImageForm(instance=Galery.objects.get(person_id=id))
    person_form = PersonForm(instance=Person.objects.get(id=id))

    if request.method == "POST":

        user_form = UserForm(request.POST, instance=User.objects.get(id=users_id))
        person_form = PersonForm(request.POST, instance=Person.objects.get(id=id))
        image_form = ImageForm(request.POST, request.FILES,instance=Galery.objects.get(person_id=id))

        if user_form .is_valid() and image_form.is_valid() and person_form.is_valid():
            user_form .save()
            person_form.save()
            image_form.save()

            return HttpResponseRedirect('{}?sent=True'.format(reverse('edit_person', kwargs={'id': id})))

    return render(request, 'person_add.html',
                   {"user_form": user_form,
                    "id": id,
                    "image_form": image_form,
                    "person_form": person_form,
                    'sent': request.GET.get('sent', False)})