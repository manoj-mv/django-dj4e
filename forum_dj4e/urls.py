from django.urls import path
from django.urls import reverse_lazy

from . import views

app_name='forum_dj4e'

urlpatterns = [
    path('',views.ForumIndexView.as_view(),name='forum_index'),
    path('create/',views.CreateForumView.as_view(success_url=reverse_lazy('forum:forum_index')),name='forum_create'),
    path('update/<int:pk>/',views.UpdateForumView.as_view(success_url=reverse_lazy('forum:forum_index')),name='forum_update'),
    path('delete/<int:pk>/',views.DeleteForumView.as_view(success_url=reverse_lazy('forum:forum_index')),name='forum_delete'),
    path('detail/<int:pk>/',views.DetailForumView.as_view(),name='forum_detail'),
    path('comment-create/<int:pk>/',views.CommentCreate.as_view(),name='comment_create'),
    path('comment/delete/<int:pk>/',views.CommentDeleteView.as_view(),name='comment_delete'),
]

