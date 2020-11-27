from django.shortcuts import render,get_object_or_404,redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.mixins  import LoginRequiredMixin
from django.urls import reverse


from .owner import OwnerListView,OwnerDetailView,OwnerCreateView,OwnerUpdateView,OwnerDeleteView
from .forms import CommentForm
from .models import Forum,Comment
# Create your views here.

class ForumIndexView(OwnerListView):
    model=Forum

class CreateForumView(OwnerCreateView):
    model = Forum
    fields= ['title','text']

class UpdateForumView(OwnerUpdateView):
    model = Forum
    fields= ['title','text']

class DeleteForumView(OwnerDeleteView):
    model=Forum

class DetailForumView(OwnerDetailView):
    model=Forum
    secondary_model=Comment
    def get_context_data(self, **kwargs):
        print('Enter get context')
        context = super().get_context_data(**kwargs)
        context["comment_form"] = CommentForm()
        print('forum key:',self.kwargs['pk']) 
        comments = self.secondary_model.objects.filter(forum=self.kwargs['pk']).order_by('-updated_at')
        # print(comments)
        context['comment_list'] = comments
        # print(context)
        return context

class CommentCreate(LoginRequiredMixin, View):
    def post(self,request,pk):
        f = get_object_or_404(Forum,pk=pk)
        print('Entered comment create view')
        comment = Comment(text=request.POST['text'],owner=request.user,forum = f)
        # print(comment)
        comment.save()
        return redirect(reverse('forum:forum_detail' , args=(pk,)))


class CommentDeleteView(OwnerDeleteView):
    model = Comment

    def get_success_url(self):
        print('Entered get_success_url method')
        # print(self.object)
        forum = self.object.forum
        print('forum:',forum)
        return reverse('forum:forum_detail',args=[forum.id])
