from django.shortcuts import render, get_object_or_404
from .models import Person
from .models import Galery
from .forms import UserForm, ImageForm, PersonForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views import generic


@login_required(login_url='/login')
def person(request, id):
    """
    Функция отображения профиля персоны
    """
    person = get_object_or_404(Person, id=id)
    image = Galery.objects.filter(person_id=id)

    return render(request, 'person.html',
                  {"person": person,
                   "image": image,
                   })


@login_required(login_url='/login')
def add_person(request, id):
    """
      Функция добавления профиля персоны
      user_form -  работает из админки и содержит поля username и пароля пользвоателя
      image_form - содержит фотографию персоны из модели галереи
      person_form -  содержит поля из модели персоны
    """
    user_form = UserForm()
    image_form = ImageForm()
    person_form = PersonForm()

    if request.is_ajax():
        """
        Если запрос на бэкенд , это ajax запрос, 
        то бэкенд валидирует данные введйнные пользователем в форму телефона - user_form
        """
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            return JsonResponse({'s': True})
        else:
            return JsonResponse({'error': user_form.errors})

    if request.method == "POST":

        user_form = UserForm(request.POST)
        person_form = PersonForm(request.POST)
        image_form = ImageForm(request.POST, request.FILES)

        if user_form.is_valid() and image_form.is_valid() and person_form.is_valid():
            # Проверяется валидность форм, валидаторы задаются в файле forms.py
            last_id = Person.objects.latest('id').id  # Последняя персона
            last_id1 = User.objects.latest('id').id  # Последний телефон в базе
            password = "empty_password"
            # Сохранение номера в базе данных с прописанным паролем( Пароль роли не играет и не валидируется)
            new_user = User.objects.create_user(**user_form.cleaned_data, id=int(last_id1)+1, password=password)
            new_user.person_id = int(last_id+1)
            new_person = person_form.save(commit=False,)
            new_person.id = last_id + 1  # Поиск ещё не занятого id пользователя
            new_person.users = new_user
            new_person.save()   # Сохранение пользователя со всеми введёнными данными
            new_image = image_form.save(commit=False)
            new_image.person_id = last_id+1
            new_image.users = new_user
            new_image.save()  # Сохранение фото пользователя

            user = authenticate(
                #  Вход пользователя в свою учтённыу запись
                username=user_form.cleaned_data['username'],
                password=password
            )
            login(request, user)

            return HttpResponseRedirect('{}?sent=True'.format(reverse('add_person', kwargs={'id': id})))

    return render(request, 'person_add.html',
                  {"user_form": user_form,
                   "id": id,
                    "image_form": image_form,
                    "person_form": person_form,
                    'sent': request.GET.get('sent', False)})

@login_required(login_url='/login')
def edit_person(request, id):
    """
      Функция редактирования персоны
      users_id - id выбранного пользователя
      user_form -  работает из админки и содержит поля username и пароля пользвоателя
      image_form - содержит фотографию персоны из модели галереи
      person_form -  содержит поля из модели персоны
    """

    users_id = Person.objects.get(id=id).users_id
    user_form = UserForm(instance=User.objects.get(id=int(users_id)))
    try:
        #  Если у пользователя нет изображения, тоо вызывается ошибка и форме присваивается знаечние None
        ImageForm2 = Galery.objects.get(person_id=id)
    except:
        ImageForm2 = None
    image_form = ImageForm(instance=ImageForm2)
    person_form = PersonForm(instance=Person.objects.get(id=id))

    if request.is_ajax():
        """
        Если запрос на бэкенд , это ajax запрос, 
        то бэкенд валидирует данные введйнные пользователем в форму телефона - user_form
        """
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            return JsonResponse({'s': True})
        else:
            return JsonResponse({'error': user_form.errors})

    if request.method == "POST":
        user_form = UserForm(request.POST, instance=User.objects.get(id=users_id))
        person_form = PersonForm(request.POST, instance=Person.objects.get(id=id))
        try:
            #  Если у пользователя нет изображения, тоо вызывается ошибка и форме присваивается знаечние None
            image_form = ImageForm(request.POST, request.FILES,instance=ImageForm2)
        except:
            image_form = ImageForm (request.POST, request.FILES, instance=Galery.objects.get())

        if user_form .is_valid() and image_form.is_valid() and person_form.is_valid():
            # Проверяется валидность форм, валидаторы задаются в файле forms.py
            # Так как это редактирование , никаких доп проверок и созданий заново не требуется
            user_form .save()
            person_form.save()
            new_image = image_form.save(commit=False)
            new_image.person_id = id
            new_image.save()
            return HttpResponseRedirect('{}?sent=True'.format(reverse('edit_person', kwargs={'id': id})))

    return render(request, 'person_edit.html',
                   {"user_form": user_form,
                    "id": id,
                    "image_form": image_form,
                    "person_form": person_form,
                    'sent': request.GET.get('sent', False)})


from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class PersonView(generic.ListView):
    model = Person
    template_name = 'person_main.html'
    queryset = Person.objects.filter()[:100]
    context_object_name = 'all_persons'

    @method_decorator(login_required(login_url='/login'))
    def dispatch(self, *args, **kwargs):
        return super(PersonView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        # В первую очередь получаем базовую реализацию контекста
        context = super(PersonView, self).get_context_data(**kwargs)
        # Добавляем новую переменную к контексту и иниуиализируем ее некоторым значением
        context['image'] = Galery.objects.filter(person_id=2)
        return context