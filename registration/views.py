from django.shortcuts import render
from person.models import Person
from person.forms import UserForm, SmsForm, UsersForm2
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .smsc_api import *
import uuid
from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import redirect


def my_random_string(string_length=10):
    """Возвращает случайную строку, нужно для отправки кода смс"""
    random = str(uuid.uuid4())  # конвертирование UUID4 в строку.
    random = random.upper()
    random = random.replace("-", "")
    return random[0:string_length]


def registration(request):
    """
         Функция регистрации профиля персоны
         user_form -  работает из админки и содержит поле username пользвоателя
         sms_form -  Нужна для обработки кода смс
    """
    user_form = UserForm()
    sms_form = SmsForm()
    disabled, disabled2 = "", "disabled"  # Параметры кнопок,которые передаются в html

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

    if request.method == "POST" and 'code' in request.POST:

        user_form = UserForm (request.POST)

        if user_form.is_valid():
            #  Отправка сообщения и валидация номера
            smsc = SMSC()  # Иницилизация класса отправки смс стороннего сервиса
            phone = user_form.cleaned_data['username']  # Форма ввода телефона
            mes = (my_random_string(4))  # смс пароль
            print(mes)
            Sms_message = Person(id=1, sms_mes=mes)  # Сохранения пароля в модель - sms_mes
            Sms_message.save()
            # counter = ['19', '1', '0.9', '194.4' ] #  Симуляция успешнйо отправки смс, для дэбага
            # d = [ '-1' ]
            counter = smsc.send_sms(phones=phone, message=mes, sender="me")  # Отправка смс с
            # введёными данными пользователя
            status_phone = smsc.get_status(phone=phone, id=counter[0])
            print(status_phone)

            if len(counter)<3 and status_phone[0] != "-1":
                #  Проверка со стороны сервиса SMSC на валидность номера
                messages.error(request, "Такого номера не существует    ")

            else:
                messages.success(request, "Код отправлен!")
                disabled = "disabled"
                disabled2 = ""

    if request.method == "POST" and 'reg' in request.POST:

        user_form = UserForm(request.POST)
        sms_form = SmsForm(request.POST)
        if user_form.is_valid () and sms_form.is_valid():
            get_id_first_person = Person.objects.get(id=1)  # Получение пароля из смс
            # ПРоверка совпадает ли код отправленный персоне и код введенный пользователем в форме
            if str(get_id_first_person.sms_mes) == sms_form.cleaned_data['sms_mes']:
                # создание и аутентификаци персоны по введёным данным пользователя
                last_id = User.objects.latest('id').id  # Последний телефон в БД
                last_i = Person.objects.latest('id').id  # Последняя персона в БД
                password = "empty_password"
                # СОхранение номера телефона пользователя в модели
                User.objects.create_user(**user_form.cleaned_data, id=int(last_id)+1, password=password)
                create_person = Person(users_id = last_id+1, id = last_i+1) # ПРисваивание id новому пользователю
                create_person.save()
                user = authenticate(
                    username=user_form.cleaned_data[ 'username' ],
                    password=password
                )
                login(request, user)
                messages.success (request, "Вы успешно зарегестрированы!")
                # Перенаправление на Добавление ФИО. фотографии и остальных данных для персоны
                return redirect('edit_person', id=last_i+1)
            else:
                messages.error(request, "Вы ввели неверный код!")
                disabled2 = ""
    return render(request, 'sign_ip.html',
                   {"user_form": user_form,
                    "sms_form": sms_form,
                    "id": id,
                    "disabled": disabled,
                    "disabled2":disabled2})


def MyLoginView(request):
    """
         Функция входа пользователя на сайт
         user_form -  работает из админки и содержит поле username пользвоателя
         user_form -  работает из админки и содержит поле username пользвоателя
         sms_form -  Нужна для обработки кода смс
       """
    user_form = UsersForm2()
    sms_form = SmsForm()
    disabled,disabled2 = "","disabled"

    if request.is_ajax():
        """
       Если запрос на бэкенд , это ajax запрос, 
       то бэкенд валидирует данные введйнные пользователем в форму телефона - user_form
       Так же после этого идёт проверка что такой пользователь существует       
       """
        user_form = UsersForm2(request.POST)
        if user_form.is_valid():
            if User.objects.filter(username=user_form.cleaned_data['username']).exists():
                return JsonResponse({'s': True})
            else:
                return JsonResponse({'error': {"username": "Такого номера в базе не существует!"}})
        else:
            return JsonResponse({'error': user_form.errors})

    if request.method == "POST" and 'code' in request.POST:
        user_form = UsersForm2(request.POST)
        if user_form.is_valid():
            # проверка существует ли пользователь с таким номером или нет
            if User.objects.filter(username=user_form.cleaned_data['username']).exists():
                # Отправка сообщения и валидация номера
                smsc = SMSC()  # Иницилизация класса отправки смс стороннего сервиса
                phone = user_form.cleaned_data[ 'username' ]  # Форма ввода телефона
                mes = my_random_string(4)  # смс пароль
                print(mes)
                Sms_message = Person(id=1, sms_mes=mes)  # Сохранения пароля в модель - sms_mes
                Sms_message.save()
                #counter = [ '19', '1', '0.9', '194.4' ]
                #d = [ '-1' ]
                # Отправка смс с введёными данными пользователя
                counter = smsc.send_sms(phones=phone, message=mes, sender="me")
                phone_status = smsc.get_status(phone=phone, id=counter[0])  # ПРоверка статуса отправки смс

                if len(counter) < 3 and phone_status[ 0 ] != "-1":
                    #  Проверка со стороны сервиса SMSC на валидность номера
                    messages.error(request, "Вы ввели неверный телефон!")
                else:
                    messages.success (request, "Код отправлен!")
                    disabled = "disabled"
                    disabled2 = ""
            else:
                messages.error (request, "Такого номера в базе не существует!")

    if request.method == "POST" and 'reg' in request.POST:

        user_form = UsersForm2(request.POST)
        sms_form = SmsForm (request.POST)
        if user_form.is_valid () and sms_form.is_valid ():
            password = "empty_password"
            # аутентификация пользователя
            user = authenticate(
                username=user_form.cleaned_data['username'],
                password=password
            )
            if user is not None:
                # Проверка валидности пользователя
                get_id_first_person = Person.objects.get(id=1)
                # ПРоверка совпадает ли код отправленный персоне и код введенный пользователем в форме
                if str(get_id_first_person.sms_mes) == sms_form.cleaned_data['sms_mes']:
                    messages.success (request, "Вы успешно залогинили!")
                    # Перенаправление пользователя на его профиль
                    login(request, user)
                    current_user = request.user.personshop.id
                    return redirect('person', id=current_user)
                else:
                    messages.error(request, "Вы ввели неверный код!")
                disabled2 = ""

    return render (request, 'login.html',
                   {"user_form": user_form,
                    "sms_form": sms_form,
                    "id": id,
                    "disabled": disabled,
                    "disabled2":disabled2})


def admin_add_person(request):
    """
          Функция отображения всех данных пользователей
    """

    return render (request, 'admin_add.html', {"user_form": Person.objects.all()})



