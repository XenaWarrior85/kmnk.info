from django.db import models


class Person(models.Model):
    first_name = models.CharField('Имя', max_length=100, null=True, blank=True)
    second_name = models.CharField('Фамилия', max_length=100, null=True, blank=True)
    third_name = models.CharField('Отчество', max_length=100, null=True, blank=True)
    birthday = models.DateField('Дата рождения', null=True, blank=True)

    def __str__(self):
        return '{second_name} {first_name} {third_name}({birthday})'.format(
            first_name=self.first_name,
            second_name=self.second_name,
            third_name=self.third_name,
            birthday=self.birthday.strftime('%d-%m-%y')
        )

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'


class Galery(models.Model):
    image = models.ImageField('Фото', upload_to='person_photo', null=True, blank=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, related_name='galery')

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галерея'
