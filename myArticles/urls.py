from django.urls import path
from . import views
from django.urls import reverse_lazy



app_name="myArticles"

urlpatterns = [
    path('',views.indexView.as_view(),name="index"),
    path('create/',views.ArticleCreate.as_view(success_url=reverse_lazy('articles:index')),name='article_create'),
    path('edit/<int:pk>',views.ArticleUpdate.as_view(success_url=reverse_lazy('articles:index')),name='article_update'),
    path('delete/<int:pk>',views.ArticleDelete.as_view(success_url=reverse_lazy('articles:index')),name='article_delete'),
    
    
]
