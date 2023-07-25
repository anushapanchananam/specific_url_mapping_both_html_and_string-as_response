from django.urls import path
from app3.views import *
app_name='any thing'

urlpatterns=[
    path('five/', five, name = 'five'),
    path('six', six, name = 'six'),
    path('saila/', saila, name = 'saila'),
]