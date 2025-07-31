from django.urls import path
from . import views

urlpatterns = [
    path('', views.note_list, name='note_list'),
    path('add/', views.add_note, name='add_note'),
    path('complete/<int:note_id>/', views.mark_completed, name='mark_completed'),
    path('remove/<int:note_id>/', views.remove_task, name='remove_task'),


]
