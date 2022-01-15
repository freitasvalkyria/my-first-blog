#importando as views do aplicativo blog 
from django.urls import path
from . import views

# Atribuindo uma view chamada "post_list" à URL raíz.
# Este padrão dirá ao Django que views.post_list é o lugar correto aonde ir se 
# alguém entra em seu site pelo endereço 'http://127.0.0.1:8000 /'.
# name='post_list' é o nome da URL que será usado para identificar a view
urlpatterns = [
    path('', views.post_list, name='post_list'),
]