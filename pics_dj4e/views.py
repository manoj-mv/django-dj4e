from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from .owner import OwnerCreateView,OwnerListView,OwnerUpdateView,OwnerDetailView,OwnerDeleteView
from .models import pic
class IndexView(OwnerListView):
    model=pic
    
class Pic_CreateView(OwnerCreateView):
    model=pic
    fields=['name','img']

class PicEditView(OwnerUpdateView):
    model=pic
    fields=['name','img']

class PicDetailView(OwnerDetailView):
    model=pic


class PicDeleteView(OwnerDeleteView):
    model=pic