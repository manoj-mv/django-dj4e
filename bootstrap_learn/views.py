from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
# Create your views here.

class IndexView(View):
    def get(self,request):
        return render(request,'bootstrap_learn/index.html')

class AboutView(View):
    def get(self,request):
        return render(request,'bootstrap_learn/aboutus.html')