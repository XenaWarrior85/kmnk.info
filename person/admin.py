from django.contrib import admin
from .models import Person, Galery,Transaction, Price, TAG


class GaleryInline(admin.TabularInline):

    model = Galery
    extra = 1
    verbose_name = 'Фото'
    verbose_name_plural = 'Фото'
    classes = ('collapse',)


class PersonAdmin(admin.ModelAdmin):

    inlines = [GaleryInline,]


admin.site.register(Person, PersonAdmin)

admin.site.register(Transaction)

admin.site.register(Price)

admin.site.register(TAG)
