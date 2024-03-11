from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import LoginForm
from part.views import sold_parts

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(
        template_name='core/login.html',
        authentication_form=LoginForm,
    ), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('history/', sold_parts, name='history'),
]