from django.contrib import admin
from .models import Game, Buyer


# Админка для модели Game
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size',)  # Отображение полей title, cost и size при отображении всех полей списком
    list_filter = ('size', 'cost',)  # Фильтрацию по полям size и cost.
    search_fields = ('title',)  # Поиск по полю title.
    list_per_page = 20  # Ограничение кол-ва записей до 20.


# Админка для модели Buyer
@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'balance', 'age', 'current_datetime',)  # Отображение полей name, balance и age при отображении всех полей списком
    list_filter = ('balance', 'age',)  # Фильтрацию по полям balance и age.
    search_fields = ('name',)  # Поиск по полю name.
    list_per_page = 30  # Ограничение кол-ва записей до 30.
    readonly_fields = ('balance',)  # Доступным только для чтения поле balance.

    # Разбиение полей на секции
    fieldsets = (
        (None, {
            'fields': ('name', 'age', 'balance')
        }),
    )
