from django.contrib import admin

from .models import Person, Galery


class GaleryInline(admin.TabularInline):
    model = Galery
    extra = 1
    verbose_name = 'Фото'
    verbose_name_plural = 'Фото'
    classes = ('collapse',)


class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'second_name', 'third_name', 'birthday')
    inlines = [GaleryInline, ]


admin.site.register(Person, PersonAdmin)
