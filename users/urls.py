from django.urls import path

from django.contrib.auth.views import (
    LogoutView,
    LoginView,
)

app_name = 'users'

urlpatterns = [
    path('logout/',
         LogoutView.as_view(template_name='users/logged_out.html', extra_context={'title':'Вы вышли из своей учётной записи'}),
         name='logout'),
    path(
        'login/',
        LoginView.as_view(template_name='users/login.html', extra_context={'title':'Авторизация'}),
        name='login'),
]