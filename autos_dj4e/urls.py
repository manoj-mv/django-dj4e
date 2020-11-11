from django.urls import path

from . import views

app_name = 'autos_dj4e'
urlpatterns=[
    path('',views.indexView.as_view(),name='index'),
    path('auto/create/',views.auto_create.as_view(),name="auto_create"),
    path('auto/<int:pk>/edit/',views.auto_edit.as_view(),name='auto_edit'),
    path('auto/<int:pk>/delete/',views.auto_delete.as_view(),name="auto_delete"),
    path('make/',views.view_all_makes.as_view(),name='make_view'),
    path('make/create/',views.make_Create.as_view(),name='make_create'),
    path('make/<int:make_id>/update',
        views.make_update.as_view(),
        name='make_update'
    ),
    path('make/<int:make_id>/delete/',
        views.make_delete.as_view(),
        name="make_delete"
    ),

]