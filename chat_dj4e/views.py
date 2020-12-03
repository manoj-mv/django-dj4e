from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy,reverse
from django import forms
from django.views.generic import CreateView
from django.contrib.humanize.templatetags.humanize import naturaltime
import time

from .models import Message
from .forms import ChatForm
# Create your views here.

class IndexView(View):
    def get(self,request):
        return render(request,'chat_dj4e/index.html')

# just print json data
def json_test(request):
    data = {
        'name':'Manoj',
        'age':'25'
    }
    print(data)
    return JsonResponse(data)

# chat window 
# class ChatView(LoginRequiredMixin,CreateView):
#     model = Message
#     template_name='chat_dj4e/chat.html'
#     form_class = ChatForm
#     success_url = reverse_lazy('chat:chat_view')
#     def form_valid(self,form):
#         print('form_valid called')
#         object = form.save(commit=False)
#         object.owner = self.request.user
#         object.save()
#         return super(ChatView,self).form_valid(form)

    
class  ChatView(LoginRequiredMixin, View):
    def get(self,request):
        form = ChatForm()
        ctx={'form' : form}
        return render(request,'chat_dj4e/chat.html',ctx)
    
    def post(self,request):
        print(request)
        message = Message(text=request.POST['text'],owner = request.user)
        message.save()
        return redirect(reverse('chat:chat_view'))

class MessageList(LoginRequiredMixin,View):
    def get(self,request):
        messages = Message.objects.all().order_by('-created_at')[:10]
        print(messages)
        result = []
        for msg in messages:
            res = [msg.text,naturaltime(msg.created_at)]
            result.append(res)
        return JsonResponse(result,safe=False) 

