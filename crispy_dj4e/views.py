from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.
from . import forms
from django.contrib import messages

class indexView(View):
    template='crispy_dj4e/index.html'
    def get(self,request):
        old_data={
          'title':'Abc',
          'mileage':20,
          'p_date':'2020-01-30'  
        }
        form= forms.demo_form(initial=old_data)
        ctx={
            'form':form
        }
        return render(request,self.template,ctx)
    
    def post(self,request):
        form = forms.demo_form(request.POST)
        if form.is_valid():
          messages.add_message(request, messages.SUCCESS, 'Data saved.')
          return redirect(reverse('home:index'))
        else:
          ctx={'form':form}
          return render(request,self.template,ctx)