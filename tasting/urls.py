from django.urls import path
from . import views

urlpatterns = [
    path('', views.generate_tasting_note, name='generate_tasting_note'),
]

