from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:token>/preview/', views.preview, name='preview'),
    path('<str:token>', views.redirect_to, name='redirect'),
    path('stats/', views.stats, name='stats'),
]
