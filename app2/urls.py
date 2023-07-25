from django.urls import path
from app2.views import *
app_name='nothing'

urlpatterns=[
    path('three/', three, name = 'three'),
    path('four', four, name = 'four'),
    path('vyshu/', vyshu, name = 'vyshu'),
]