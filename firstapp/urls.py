from django.urls import path
from . import views

urlpatterns = [
    path('form/',views.django_form,name='form' ),
    path('model/',views.model,name='model_form' ),
]
