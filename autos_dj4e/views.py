from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView,View
# https://docs.djangoproject.com/en/3.1/ref/class-based-views/generic-editing/
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponse
from autos_dj4e.forms import MakeForm
from .models import Auto,Make
# Create your views here.

class indexView(LoginRequiredMixin,ListView):
    model=Auto
    template_name='autos_dj4e/index.html'
    context_object_name='auto_list'

    # Add additional context
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['make_count']= Make.objects.all().count()
        return context



class view_all_makes(LoginRequiredMixin,ListView):
    model=Make
    template_name='autos_dj4e/make_view.html'
    context_object_name='make_list'



class make_Create(LoginRequiredMixin,View):
    template="autos_dj4e/make_create_form.html"
    success_url=reverse_lazy('autos_dj4e:index')
    def get(self, request):
        form = MakeForm()
        ctx = {'form': form}
        return render(request, self.template, ctx)
    
    def post(self,request):
        form = MakeForm(request.POST)
        if not form.is_valid() :
            ctx={
                'form' : form
            }
            return render(request,self.template,ctx)
        form.save()
        return redirect(self.success_url)
        


class make_update(LoginRequiredMixin,View):
    template='autos_dj4e/make_update.html'
    success_url = reverse_lazy('autos_dj4e:make_view')

    def get(self,request,make_id):
        make_data=get_object_or_404(Make,pk=make_id)
        form = MakeForm(instance=make_data)
        ctx={'form':form}
        return render(request,self.template,ctx)

    def post(self,request,make_id):
        check_existence_make=get_object_or_404(Make,pk=make_id)
        form = MakeForm(request.POST,instance=check_existence_make)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        else:
            ctx={'form':form}
            return render(request,self.template,ctx)

        
        
class make_delete(LoginRequiredMixin,View):
    # template name can be any unless we use generic edit views(CreatView,DeleteView etc..)              
    template='autos_dj4e/make_confirm_delete.html'
    success_url=reverse_lazy('autos_dj4e:make_view')
    model=Make
    def get(self,request,make_id):
        # check whether the entry  exist in db otherwise raise http404
        check_existence_make = get_object_or_404(self.model,pk=make_id)
        # context passed to delete confirm page
        ctx ={'make_to_delete':check_existence_make}
        return render(request,self.template,ctx)
    
    def post(self,request,make_id):
        # check whether the entry  exist in db otherwise raise http404
        check_make = get_object_or_404(self.model,pk=make_id)
        # deleting the entry whose pk=make_id
        check_make.delete() 
        # redirect to a success_url
        return redirect(self.success_url)

# generic edit view: CreateView 
class auto_create(LoginRequiredMixin,CreateView):
    model=Auto
    fields=['name','make','mileage','comments']
    success_url=reverse_lazy('autos_dj4e:index')
    op='Create'
    # default name is '[modelName]_form'.Here 'auto_form'
    # if we need to explicitly specify teemplate use 'template_name attribute
    # eg: template_name='autos_dj4e/auto_form_test.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['operation']= self.op
        context['submit_val']=self.op
        return context

# generic edit view : UpdateView
class auto_edit(LoginRequiredMixin,UpdateView):
    model=Auto
    fields="__all__"
    success_url=reverse_lazy('autos_dj4e:index')
    op='Edit'

    # additional context
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['operation']= self.op
        context['submit_val']='Update'
        return context

class auto_delete(LoginRequiredMixin,DeleteView):
    model=Auto
    success_url=reverse_lazy('autos_dj4e:index')