from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm
from .models import Buyer, Game

# Create your views here.
users = Buyer.objects.all()
print(users.query)


class Template(TemplateView):
    template_name = "menu.html"


def func_platform(request):
    return render(request, "platform.html")


def func_magazin(request):
    digits_games = Game.objects.all()
    context = {'digits_games': digits_games}
    return render(request, 'games.html', context)


def func_korzina(request):
    return render(request, "cart.html")


def sign_up_by_html(request):
    usernames = [i.name for i in users]
    i = 0
    info = {'error': []}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        print(f'Username: {username}')
        print(f'Password: {password}')
        print(f'Repeat password: {repeat_password}')
        print(f'Age: {age}')
        if username not in usernames and password == repeat_password and int(age) >= 18:
            Buyer.objects.create(name=username, balance='100', age=age)
            context = {'username': username}
            return render(request, 'register_done.html', context)

        elif username in usernames:
            i += 1
            info[f'error {i}'] = HttpResponse('Пользователь уже существует', status=400, reason='repeated login')
            return HttpResponse('Пользователь уже существует', status=400, reason='repeated login')

        elif password != repeat_password:
            i += 1
            info[f'error {i}'] = HttpResponse('Пароли не совпадают', status=400, reason='non-identical passwords')
            return HttpResponse('Пароли не совпадают', status=400, reason='non-identical passwords')
        elif int(age) < 18:
            i += 1
            info[f'error {i}'] = HttpResponse(
                f'Вы должны быть старше 18', status=400, reason='insufficient age')
            return HttpResponse(f'Вы должны быть старше 18', status=400, reason='insufficient age')

    context = {'info': info}
    return render(request, 'register_user.html', context)


def sign_up_by_django(request):
    current_datetime = datetime.now()
    usernames = [i.name for i in users]
    i = 0
    info = {'error': []}
    if request.method == 'GET':
        form = ContactForm()
        context = {'form': form}
        return render(request, 'register_done.html', context)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if username not in usernames and password == repeat_password and int(age) >= 18:
                Buyer.objects.create(name=username, balance='100', age=age)
                context = {'username': username}
                return render(request, 'menu.html', context)

            elif username in usernames:
                i += 1
                info[f'error {i}'] = HttpResponse('Пользователь уже существует', status=400, reason='repeated login')
                return HttpResponse('Пользователь уже существует', status=400, reason='repeated login')

            elif password != repeat_password:
                i += 1
                info[f'error {i}'] = HttpResponse('Пароли не совпадают', status=400, reason='non-identical passwords')
                return HttpResponse('Пароли не совпадают', status=400, reason='non-identical passwords')
            elif int(age) < 18:
                i += 1
                info[f'error {i}'] = HttpResponse(
                    f'Вы должны быть старше 18', status=400, reason='insufficient age')
                return HttpResponse(f'Вы должны быть старше 18', status=400, reason='insufficient age')

        else:
            form = ContactForm()
        return render(request, 'register_user.html', {'form': form})
