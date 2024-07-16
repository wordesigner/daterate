from django.urls import path
from . import views

urlpatterns = [
    path('form', views.picker, name='datedata'),
    path('result', views.result),
    path('', views.onboard)
]