from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import TemplateView
from task1.forms import UserRegister
from .models import *


class Main_platform(TemplateView):
    template_name = 'fourth_task/platform.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context


class Games_Class(TemplateView):
    template_name = 'fourth_task/games.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        games_all = Game.objects.all()
        context['title'] = 'Игры'
        context['games'] = games_all
        context['asd'] = 'cart'
        items_per_page = self.request.GET.get('items_per_page', '3')
        items_per_page = int(items_per_page) if items_per_page.isdigit() else 3

        # Создаем пагинатор
        paginator = Paginator(games_all, items_per_page)

        # Получаем номер страницы из GET-запроса, по умолчанию 1
        page_number = self.request.GET.get('page', '1')
        page_obj = paginator.get_page(page_number)

        # Добавляем данные в контекст
        context['page_obj'] = page_obj
        context['items_per_page_options'] = [1, 2, 3, 5, 10]
        context['items_per_page'] = items_per_page

        return context


class Cart_Class(TemplateView):
    template_name = 'fourth_task/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Корзина'
        context['cart_content'] = "Извините корзина пуста"
        return context


class User_Register(TemplateView):
    template_name = 'fifth_task/registration_page.html'

    def get(self, request):
        form = UserRegister()
        return render(request, self.template_name, {'form': form, 'title': 'Страница регистрации'})

    def post(self, request):
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            age = form.cleaned_data['age']
            new_user = sign_up_by_django(username, password, age)
            if new_user != 'Создан':
                username = f'такой пользователь уже существует'
                return render(request, self.template_name, {'form': form, 'username': username})
            elif new_user == 'Создан':
                username = f'Новый пользователь создан'
                return render(request, self.template_name, {'form': form, 'username': username})

            else:
                username = f'Приветствуем, {new_user}'
                return render(request, self.template_name, {'form': form, 'username': username})

        return render(request, self.template_name, {'form': form, 'title': 'Страница регистрации'})


dict_user = {'qwe': 12345678}


def sign_up_by_django(username, password, age):
    try:
        user = Buyer.objects.get(name=username)
        print(f'Пользователь найден: {user}')
        return user
    except Buyer.DoesNotExist:
        Buyer.objects.create(name=username, balance=0, age=age)
        user_create = 'Создан'
        return user_create
