from django.urls import path
from . import views


app_name = 'recipes'

urlpatterns = [
    path('create/', views.recipe_create, name='create'),
    path('detail/<int:id>/<slug:slug>', views.recipe_detail, name='detail'),
    path('', views.recipe_list, name='list'),
    path('update/<int:id>/', views.recipe_update, name='update'),
    path('delete/<int:id>/', views.recipe_delete, name='delete'),
]
