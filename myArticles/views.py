from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic import ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .owner import OwnerCreateView,OwnerUpdateView,OwnerDeleteView

from .models import Article

# Create your views here.


class indexView(LoginRequiredMixin, ListView):
    model=Article

class ArticleCreate(OwnerCreateView):
    model=Article
    fields=['title','text']

class ArticleUpdate(OwnerUpdateView):
    model=Article
    fields=['title','text']

class ArticleDelete(OwnerDeleteView):
    model=Article


