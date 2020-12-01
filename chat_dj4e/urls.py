from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'chat_dj4e'

urlpatterns = [
    path('',views.IndexView.as_view(),name='chat_index'),
    path('syntax',TemplateView.as_view(template_name='chat_dj4e/syntax.html'),name='syntax'),
    path('json_test',views.json_test,name='json_test'),
    path('chat_window',views.ChatView.as_view(),name = 'chat_view'),
]
