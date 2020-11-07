from django.urls import path
from . import views

app_name ='authz_dj4e'
urlpatterns = [
    path('',views.index.as_view(),name='index'),
    path('open/',views.openView.as_view(),name='open'),
    path('manual_protect/',views.manualProtect.as_view(),name="manual"),
    path('mixin_protect/',views.protectView.as_view(),name='protect'),
    path('python',views.DumpPython.as_view(),name='python'),    
]