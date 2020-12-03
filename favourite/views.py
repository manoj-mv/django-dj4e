from django.shortcuts import render
from django.views import View
from django.urls import reverse_lazy
# Create your views here.

from .models import Thing,Fav
from forum_dj4e.owner import OwnerCreateView,OwnerDeleteView,OwnerListView,OwnerUpdateView
class ThingListView(OwnerListView):
    model = Thing
    template_name = 'favourite/index.html'

    def get(self,request):
        thing_list = Thing.objects.all()
        print(thing_list)
        usr = request.user
        # print(dir(usr))
        # print(fvrt_list)
        try:
            fav_list = Fav.objects.all().filter(user=usr)
        except:
            fav_list=None
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

