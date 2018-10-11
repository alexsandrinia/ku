
from django.urls import path
from . import views

urlpatterns = [
    path('add', views.ClientCreateView.as_view(), name = 'client-create'),
    path('', views.ClientListView.as_view(), name = 'client-list'),
]