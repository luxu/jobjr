from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crawler/', views.crawler, name='crawler'),
    path('crawler/', views.crawler, name='crawler_vagas'),
    path('salvar/', views.salvar, name='salvar'),
    path('salvar_api/', views.salvar_api, name='salvar_api'),
]
