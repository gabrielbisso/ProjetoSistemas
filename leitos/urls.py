from django.urls import path
from . import views

urlpatterns = [
    path('leitos/', views.leitos, name="leitos")
]