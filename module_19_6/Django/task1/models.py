from django.db import models


# Create your models here.
# Модели с отношением "многие ко многим"
class Buyer(models.Model):  # модель представляющая покупателя
    id = models.AutoField(auto_created=True, primary_key=True, verbose_name='id')
    name = models.CharField(max_length=30)  # имя покупателя(username аккаунта)
    balance = models.IntegerField()  # баланс(DecimalField)
    age = models.IntegerField()  # возраст
    current_datetime = models.DateTimeField(null=True, blank=True, auto_now_add=True, verbose_name="Дата регистрации")

    def __str__(self):
        return f'{[self.name, self.balance, self.age]!r}'


class Game(models.Model):  # модель представляющая игру
    id = models.AutoField(auto_created=True, primary_key=True, verbose_name='id')
    title = models.CharField(max_length=300)  # название игры
    cost = models.IntegerField()  # цена(DecimalField)
    size = models.IntegerField()  # размер файла
    description = models.TextField()  # описание(неограниченное кол-во текста)
    age_limited = models.BooleanField(default=False)  # Возрастной рейтинг: (BooleanField, по умолчанию False)
    buyer = models.ManyToManyField(Buyer, related_name='buyers')  # покупатель обладающий игрой (ManyToManyField).

    # У каждого покупателя может быть игра и у каждой игры может быть несколько обладателей.


class News(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, verbose_name='id')
    title = models.CharField(max_length=60)
    content = models.TextField()
    current_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{[self.title, self.content]!r}'
