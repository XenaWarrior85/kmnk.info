from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

"""
Модель ПЕРСОНА, ТЭГ, ГРУППА
"""


class Group(models.Model):
    # Группы , которые выбираются для тэгов, содержат имя группы и её вес
    title = models.CharField("Название", max_length=100, null=True)
    width = models.FloatField("Вес", default=0.00, null=True, validators=[MaxValueValidator(1), MinValueValidator(0)])

    def __str__(self):
        return '{title}'.format(title=self.title)


class TAG(models.Model):
    # Тэги для персоны, с выбором имени тэга, веса тэга и группы
    tag_name = models.CharField(max_length=100, null=True)
    width = models.FloatField("Вес", default=0.00, null=True, validators=[MaxValueValidator(1), MinValueValidator(0)])
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True,  blank=False)

    def __str__(self):
        return '{tag_name}'.format(tag_name=self.tag_name)


class Person(models.Model):
    # Модели которые хранят основные данные пользователя, которые отображаютс в его профиле

    # Телефон пользователя
    users = models.OneToOneField(User, on_delete=models.CASCADE, related_name='personshop',  null=True)
    first_name = models.CharField('Имя', max_length=100, null=True, blank=False)
    second_name = models.CharField('Фамилия', max_length=100, null=True, blank=False)
    third_name = models.CharField('Отчество', max_length=100, null=True, blank=False)
    birthday = models.DateField('Дата рождения', null=True, blank=True)
    # Смс сообщение , которое присылается пользователю при входе и регистрации
    sms_mes = models.CharField('Сообщение', max_length=100, null=True, blank=True)
    wallet = models.DecimalField('Кошелёк', default=0.00, max_digits=9, decimal_places=2)
    reputation = models.FloatField(
        default=3.5,
        validators=[MaxValueValidator(5), MinValueValidator(2)]
     )
    tag = models.ForeignKey(TAG, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '{second_name} {first_name} {third_name}({birthday}){sms_mes}'.format (
            first_name=self.first_name,
            second_name=self.second_name,
            third_name=self.third_name,
            birthday=self.birthday,
            sms_mes = self.sms_mes
        )

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'


"""
# Модель ТРАНЗАКЦИЯ, ЦЕНА , ЕДИНИЦА ИЗМЕРЕНИЯ
"""


class Units(models.Model):
    # Таблица с различными единицами измерения. Сейчас состоит из имени и самой единицы измерения
    title = models.CharField("Название", max_length=100, null=True)
    unit = models.CharField("Единица измерения", max_length=100, null=True)

    def __str__(self):
        return '{title}'.format(title=self.title)


class Price(models.Model):
    # Модель цены с названием и единицей измерения возможного товара
    title = models.CharField("Название", max_length=100)
    price = models.DecimalField("Цена",default=0, max_digits=30, decimal_places=2)
    unit_of_measurement = models.ForeignKey(Units, on_delete=models.CASCADE, null=True, blank=False)

    def __str__(self):
        return '{title}'.format(title=self.title)


class Transaction(models.Model):
    #  Модель, которая хранит все данные о транзакции

    # Время и дата транзакциии
    datetime = models.DateTimeField("Дата/время", auto_now_add=True)
    from_whom = models.ForeignKey(Person, on_delete=models.DO_NOTHING, related_name="От_кого")
    to_whom = models.ForeignKey(Person, on_delete=models.DO_NOTHING, related_name="Кому")
    summ = models.DecimalField("Сумма", max_digits=30, decimal_places=2)
    price_w = models.ForeignKey(Price,  on_delete=models.CASCADE)
    # Хранение всех состояний транзакции
    hash_amount = models.BinaryField("Хэш сумма", max_length=200, null=True)


"""
# Модель ГАЛЕРЕЯ
"""

class Galery(models.Model):
    # Модель в которой хранится соответствие персоны и его фоторгафий
    image = models.ImageField(upload_to='person_photo', null=True, blank=True, default='')
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, related_name='galery')

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'

    # Отображение пути к фотографии
    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url



