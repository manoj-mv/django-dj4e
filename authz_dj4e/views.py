from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from django.urls import reverse
from django.utils.http import urlencode
from django.contrib.auth.mixins import LoginRequiredMixin,redirect_to_login
# Create your views here.
# def index(request):
#     return render(request,'authz_dj4e/index.html')
    
class index(View):
    def get(self,request):
        return render(request,'authz_dj4e/index.html')

class openView(View):
    def get(self,request):
        return render(request,'authz_dj4e/index.html')

class manualProtect(View):
    def get(self,request):
        if not request.user.is_authenticated:
            # login_url = reverse('login')+'?'+urlencode({'next':request.path})
            # return redirect(login_url)
            return redirect_to_login(request.path)
        else:
            return render(request,'authz_dj4e/index.html')

class protectView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'authz_dj4e/index.html')

class DumpPython(View) :
    def get(self, req):
        resp = "<pre>\nUser Data in Python:\n\n"
        resp += "Login url: " + reverse('login') + "\n"
        resp += "Logout url: " + reverse('logout') + "\n\n"
        if req.user.is_authenticated:
            resp += "User: " + req.user.username + "\n"
            resp += "Email: " + req.user.email + "\n"
        else:
            resp += "User is not logged in\n"

        resp += "\n"
        resp += "</pre>\n"
        resp += """<a href="/authz">Go back</a>"""
        return HttpResponse(resp)
