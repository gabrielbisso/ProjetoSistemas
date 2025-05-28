from django.urls import path
from . import views

app_name = 'leitos'

urlpatterns = [
    path('leitos/', views.leitos, name="leitos")
]
