from django.contrib.auth import views as auth_views
from django.urls import path
from .forms import LoginForm
from . import views

app_name = 'core'
urlpatterns = [
  # path('', views.home)
  path('', views.home, name='home'),
  path('signup/', views.signup, name='signup'),
  path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
  path('logout/', views.user_logout, name='logout'),
]









