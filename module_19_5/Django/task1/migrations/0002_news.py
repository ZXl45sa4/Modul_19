# Generated by Django 5.1.4 on 2025-01-12 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.DecimalField(decimal_places=3, max_digits=100000)),
                ('current_datetime', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата регистрации')),
            ],
        ),
    ]
