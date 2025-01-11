from django.db import models


# Create your models here.
# Модели с отношением "многие ко многим"
class Buyer(models.Model):  # модель представляющая покупателя
    name = models.CharField(max_length=30)  # имя покупателя(username аккаунта)
    balance = models.DecimalField(max_digits=100000, decimal_places=2)  # баланс(DecimalField)
    age = models.IntegerField()  # возраст
    current_datetime = models.DateTimeField(null=True, blank=True, auto_now_add=True, verbose_name="Дата регистрации")

    def __str__(self):
        return self.name


class Game(models.Model):  # модель представляющая игру
    title = models.CharField(max_length=100)  # название игры
    cost = models.DecimalField(max_digits=10000, decimal_places=2)  # цена(DecimalField)
    size = models.DecimalField(max_digits=100000, decimal_places=3)  # описание(неограниченное кол-во текста)
    description = models.TextField()  # описание(неограниченное кол-во текста)
    age_limited = models.BooleanField(default=False)  # ограничение возраста 18+ (BooleanField, по умолчанию False)
    buyer = models.ManyToManyField(Buyer, related_name='buyers')  # покупатель обладающий игрой (ManyToManyField).
    # У каждого покупателя может быть игра и у каждой игры может быть несколько обладателей.
