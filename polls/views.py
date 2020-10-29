from django.shortcuts import render,get_object_or_404
from .models import Question,choice 
from django.template import loader
# Create your views here.
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.views import generic



# detailed way
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # output = ', '.join([q.question_text for q in latest_question_list])
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     # detailed way
#     # template = loader.get_template('polls/index.html')
#     # return HttpResponse(template.render(context,request))
#     #shortcut
#     return render(request,'polls/index.html',context)

# using generic ListView
class IndexPage(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

# detailed way
# def detail(request,question_id):
#     # detailed way for db access and raise error if doesnt exists
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     #shortcut
#     question = get_object_or_404(Question, pk=question_id)
#     # old way
#     # return HttpResponse("You are looking at question %s.:" % question_id)
#     # short cut
#     return render(request,'polls/detail.html',{'question':question})

# using genetic DetailView
class DetailPage(generic.DeleteView):
    model =Question
    template_name = 'polls/detail.html'

# old way
# def results(request,question_id):
#     # response = "You are looking at the results of question %s."
#     # return HttpResponse(response % question_id)
#     question = get_object_or_404(Question,pk=question_id)
#     ctx = {'question':question}
#     return render(request,'polls/results.html',ctx)

# using genetic DetailView
class ResultsPage(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request,question_id):
    # response ="You are voting on question %s."
    # return HttpResponse(response % question_id)
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError,choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request,'polls/detail.html',{'question':question,'error_message':"you didn't select a choice"})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data.
        return HttpResponseRedirect(reverse('polls:results',args=(question_id,)))


