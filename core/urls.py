from django.urls import path
from . import views


app_name = 'core'
urlpatterns = [
    path('web/', views.WebDevelopment.as_view(), name='web'),
    path('network/', views.Networking.as_view(), name='ntwrk'),
    path('ml/', views.MachineLearning.as_view(), name='ml'),
    path('android/', views.Android.as_view(),name='android'),
    ]
