from django.urls import path
from Calculator.views import add, subtract, multiply, divide

# note: implement this file inside of Calculator/urls.py

urlpatterns = [
    path('add/', add, name='add'),
    path('subtract/', subtract, name='subtract'),
    path('multiply/', multiply, name='multiply'),
    path('divide/', divide, name='divide'),
]

