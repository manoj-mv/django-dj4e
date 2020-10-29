from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse,reverse_lazy
# Create your views here.

def index(request):
    # page = loader.get_template('samples/tags.html') 
    url =  reverse_lazy('samples:ext2')
    dic = {
        'a' : 12,
        'lst' : ['a','b','c'],
    }
    context = {
        'url' : url,
        'dic' : dic,
    }
    return render(request,'samples/tags_ext.html',context)
def ext2(request):
    url=reverse_lazy('samples:index')
    ifchanged_url = reverse_lazy('samples:ifchanged')
    txt='<p>You are <em>pretty</em> smart!</p>'
    lst = [1,2,3,4,5]
    ctx= {
        'url':url,
        'ifchanged_url': ifchanged_url,
        'txt':txt,
        'lst':lst,
    }
    return render(request,'samples/tags_ext2.html',ctx)

def ifchanged_tag(request):
    lst = ['python','ruby','ruby','python','java','c#','c#','python']
    ctx ={
        'lst':lst,
    }
    return render(request,'samples/ifchanged_tag.html',ctx)

def include_tag_test(request):
    url = reverse_lazy('samples:index')
    return render(request,'samples/include_tag_test/main.html')
    

