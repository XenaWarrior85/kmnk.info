from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Person(models.Model):
    users = models.OneToOneField(User, on_delete=models.CASCADE, related_name='personshop',  null = True)
    first_name = models.CharField ('Имя', max_length=100, null=True, blank=True)
    second_name = models.CharField ('Фамилия', max_length=100, null=True, blank=True)
    third_name = models.CharField('Отчество', max_length=100, null=True, blank=True)
    birthday = models.DateField('Дата рождения', null=True, blank=True)

    def __str__(self):
        return '{second_name} {first_name} {third_name}({birthday})'.format (
            first_name=self.first_name,
            second_name=self.second_name,
            third_name=self.third_name,
            birthday=self.birthday
        )

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'


# def create_profile(sender, **kwargs):
#     if kwargs[ "created" ]:
#         Person.objects.create(users=kwargs['instance'])
#
# post_save.connect(create_profile, sender=User)


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



