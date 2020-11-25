from django.urls import path
from django.urls import reverse_lazy

from . import views


app_name='pics_dj4e'
urlpatterns = [
    path('',views.IndexView.as_view(),name="pics_index"),
    path('create/',views.Pic_CreateView.as_view(success_url=reverse_lazy('pics:pics_index')),name='pic_create'),
    path('edit/<int:pk>',views.PicEditView.as_view(success_url=reverse_lazy('pics:pics_index')),name='pic_update'),
    path('detail/<int:pk>',views.PicDetailView.as_view(),name='pic_detail'),
    path('delete/<int:pk>',views.PicDeleteView.as_view(success_url=reverse_lazy('pics:pics_index')),name='pic_delete'),
]
