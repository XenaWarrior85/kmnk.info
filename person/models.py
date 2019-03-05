from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class TAG(models.Model):
    width = models.FloatField("Вес", default=0.00, null=True)
    group = models.CharField("Группа", max_length=100, null=True)

    def __str__(self):
        return '{group}'.format(group=self.group)


class Person(models.Model):
    users = models.OneToOneField(User, on_delete=models.CASCADE, related_name='personshop',  null=True)
    first_name = models.CharField('Имя', max_length=100, null=True, blank=False)
    second_name = models.CharField('Фамилия', max_length=100, null=True, blank=False)
    third_name = models.CharField('Отчество', max_length=100, null=True, blank=False)
    birthday = models.DateField('Дата рождения', null=True, blank=True)
    sms_mes = models.CharField('Сообщение', max_length=100, null=True, blank=True)
    wallet = models.DecimalField('Кошелёк', default=0.00, max_digits=30, decimal_places=2)
    reputation = models.FloatField(
        default=2.0,
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


class Price(models.Model):
    title = models.CharField("Название", max_length=100)
    price = models.DecimalField("Цена", max_digits=30, decimal_places=2)
    currency = models.CharField("единица измерения", max_length=100, null=False)

    def __str__(self):
        return '{title}{currency}'.format(
            title=self.title,
            currency=self.currency
        )


class Transaction(models.Model):
    datetime = models.DateTimeField("Дата/время", auto_now_add=True)
    from_whom = models.CharField("От кого", max_length=100, null=False)
    to_whom = models.CharField("Кому", max_length=100, null=False)
    summ = models.DecimalField("Сумма", max_digits=30, decimal_places=2)
    price_w = models.ForeignKey(Price,  on_delete=models.CASCADE)
    hash_amount = models.CharField("Хэш сумма", max_length=10000, null=True)

    def __str__(self):
        return '{from_whom}{to_whom}'.format(
            from_whom=self.from_whom,
            to_whom=self.to_whom
        )


class Galery(models.Model):
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



