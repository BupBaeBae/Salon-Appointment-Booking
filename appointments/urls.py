
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book/', views.book_appointment, name='book'),
    path('cancel/', views.cancel_appointment, name='cancel'),
]
