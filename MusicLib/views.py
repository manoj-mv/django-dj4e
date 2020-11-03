from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from .models import Artist,Album,Track

# Create your views here.


# using function
# def index(request):
#     track = Track.objects.all()
#     ctx={
#         'track' : track, 
#     }
#     return render(request,'MusicLib/index.html',ctx)

# using generic views

class indexView(generic.ListView):
    template_name = 'MusicLib/index.html'
    context_object_name = 'track'
    def get_queryset(self):
        return Track.objects.all()

def detail_route(request):
    song_id = request.POST['song_id']
    # song_data = get_object_or_404(Track,pk=song_id)
    # return render(request,'MusicLib/detail.html',{'song_detail':song_data})
    return HttpResponseRedirect(reverse('MusicLib:song_detail',args=(song_id,)))
    # return render(request,'MusicLib/detail.html')
class songDetail(generic.DetailView):
    model = Track
    template_name='MusicLib/detail.html'
    context_object_name='song_detail'
    
