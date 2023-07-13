from django.urls import path
from catalog.views import home, contacts
from . import views


urlpatterns = [
    path('', home),
    path('contacts/', views.contacts, name='contacts')

]