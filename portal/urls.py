from django.urls import path
from . import views

urlpatterns = [
	path('', views.not_list, name='not_list'),
	path('detalhesdasnot/<int:pk>/', views.detalhesdasnot, name='detalhesdasnot'),
	path('nova/not', views.nova_not, name='nova_not'),
	path('not/edit<int:pk>/edit/', views.not_edit, name='not_edit'),
	path('publicar/<int:pk>/', views.publicar, name='publicar'),
	path('remover/<int:pk>/not/>', views.remover_not, name='remover_not'),
	path('areas', views.area_list, name='area_list'),
	path('detalhesdaarea/<int:pk>/', views.detalhesdaarea, name='detalhesdaarea'),
	path('nova/area', views.nova_area, name='nova_area'),
	path('area/edit<int:pk>/edit/', views.area_edit, name='area_edit'),
	path('ativar/<int:pk>/', views.ativar, name='ativar'),
	path('desativar/<int:pk>/', views.desativar, name='desativar'),
	path('remover/<int:pk>/area/>', views.remover_area, name='remover_area'),
]