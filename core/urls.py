from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'core'
urlpatterns = [
    path('', views.IndexView, name='index'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), {'next_page': 'settings.LOGOUT_REDIRECT_URL'}, name='logout'),
    path('signup/', views.SignUp, name='signup'),
    path('web/', views.WebDevelopment.as_view(), name='web'),
    path('network/', views.Networking.as_view(), name='ntwrk'),
    path('ml/', views.MachineLearning.as_view(), name='ml'),
    path('android/', views.Android.as_view(),name='android'),
    ]
