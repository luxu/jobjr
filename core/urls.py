from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crawler/', views.crawler, name='crawler'),
    path('crawler/', views.crawler, name='crawler_vagas')
]
