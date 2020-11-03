from django.urls import path

from . import views
app_name = 'MusicLib'
urlpatterns = [
    path('',views.indexView.as_view(),name='index'),
    path('detail/',views.detail_route,name='detail_route'),
    path('<int:pk>/',views.songDetail.as_view(),name="song_detail"),
    
]