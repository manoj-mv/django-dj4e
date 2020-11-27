from django.shortcuts import render,get_object_or_404
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import FileResponse
from django.urls import reverse
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



def stream_file(request, pk):
    print('Enter stream')
    ad = get_object_or_404(pic, id=pk)
    # response = HttpResponse()
    print(ad)
    # response['Content-Type'] = pic.content_type
    # response['Content-Length'] = len(pic.picture)
    # response.write(pic.picture)
    # return respon
    # data= open(ad.img, "rb")
    # print('data is',data)
    # response = FileResponse(data)
    print(ad.img.url)
    print(ad.img)
    url=ad.img.url
    return HttpResponse("<img src='{0}'>".format(url))