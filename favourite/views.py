from django.shortcuts import render,get_object_or_404
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.db.utils import IntegrityError

from .models import Thing,Fav
from forum_dj4e.owner import OwnerCreateView,OwnerDeleteView,OwnerListView,OwnerUpdateView
class ThingListView(OwnerListView):
    model = Thing
    template_name = 'favourite/index.html'

    def get(self,request):
        print('Executing ThingListView get()')
        fav_list=None
        thing_list = Thing.objects.all()
        # print(thing_list)
        usr = request.user
        # print(dir(usr))
        # print(fvrt_list)
        if usr.is_authenticated:
            print('user is authenticated')
            try:
                print('Entered try block')
                fav_l = Fav.objects.all().filter(user=usr)
                print('fav_l : ',fav_l)
                fav_list = [fav.thing.id for fav in fav_l]
               
                # by referencing many to many field in Thing, below commented code can also be used for access user favourites
                # l=request.user.favourite_things.values('id') 
                
            except:
                print('Entered catch block in ThingListView get()')
                fav_list=None
        print('fav_list:',fav_list)
        ctx={
            'thing_list': thing_list,
            'favourites': fav_list
        }
        return render(request,self.template_name,ctx)

class ThingCreateView(OwnerCreateView):
    model=Thing
    fields = ['title','text']
    success_url = reverse_lazy('fav:index')

class ThingUpdateView(OwnerUpdateView):
    model=Thing
    fields = ['title','text']
    success_url = reverse_lazy('fav:index')

class ThingDeleteView(OwnerDeleteView):
    model = Thing
    success_url = reverse_lazy('fav:index')

class AddFavourite(LoginRequiredMixin, View):
    def post(self,request,pk):
        print(pk)
        print(request.user)
        thing_obj = get_object_or_404(Thing,pk=pk)
        fav_obj = Fav(thing=thing_obj,user=request.user)
        print(fav_obj)
        try:
            fav_obj.save() # In case of duplicate key
        except IntegrityError as e:
            pass
        return HttpResponse()

class UnFavourite(LoginRequiredMixin, View):
    def post(self,request,pk):
        print(pk)
        print(request.user)    
        fav_obj = get_object_or_404(Fav,thing = pk,user=request.user)
        fav_obj.delete()
        print('unfavourited :',fav_obj)
        return HttpResponse()


