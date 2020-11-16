from django.urls import path

from . import views

app_name='crispy_dj4e'

urlpatterns = [
    path("",views.indexView.as_view(),name='index'),
]