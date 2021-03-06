from django.urls import path

from . import views

app_name = 'favourites'

urlpatterns = [
    path('',views.ThingListView.as_view(),name='index'),
    path('create',views.ThingCreateView.as_view(),name='thing_create'),
    path('update/<int:pk>',views.ThingUpdateView.as_view(),name='thing_update'),
    path('delete/<int:pk>',views.ThingDeleteView.as_view(),name='thing_delete'),
    path('add-to-favourite/<int:pk>',views.AddFavourite.as_view(),name="add_favourite"),
    path('unfavourite/<int:pk>',views.UnFavourite.as_view(),name='unfavourite')
]
