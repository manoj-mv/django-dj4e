from django.urls import path
from . import views

app_name = 'samples'
urlpatterns =[
    path('',views.index,name='index'),
    path('ext2',views.ext2,name='ext2'),
    path('ifchanged',views.ifchanged_tag,name='ifchanged'),
    path('include_tag',views.include_tag_test,name='include_template')
]