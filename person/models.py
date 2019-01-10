from django.db import models


class Person(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    first_name = models.CharField('Имя', max_length=100, null=True, blank=True)
    second_name = models.CharField('Фамилия', max_length=100, null=True, blank=True)
    third_name = models.CharField('Отчество', max_length=100, null=True, blank=True)
    birthday = models.DateField('Дата рождения', null=True, blank=True)

    def __str__(self):
        return '{second_name} {first_name} {third_name}({birthday})'.format(
            first_name=self.first_name,
            second_name=self.second_name,
            third_name=self.third_name,
            birthday=self.birthday
        )

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'


class Galery(models.Model):
    image = models.ImageField(upload_to='person_photo', null=True, blank=True, default='')
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, related_name='galery')

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'

    # Отображение пути к фотографии
    @property
    def image_url(self):
        if self.image and hasattr (self.image, 'url'):
            return self.image.url



