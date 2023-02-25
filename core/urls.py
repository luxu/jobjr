from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # path('crawler/', views.crawler, name='crawler'),
    # path('salvar/', views.salvar, name='salvar'),
    path('v1/crawler/', views.crawler_api, name='crawler_api'),
    path('v1/listar/', views.listar_api, name='listar_api'),
    path('v1/excluir/', views.excluir, name='excluir_api'),
    path('v1/salvar/', views.salvar_api, name='salvar_api'),
]
