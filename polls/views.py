from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.urls import reverse
from polls.models import Question,Choice
from django.template import loader
from django.views import generic

def index(request):
    listx = Question.objects.order_by('?')
    template = loader.get_template('polls/index.html')
    content = {
        'listx' : listx
    }
    return HttpResponse(template.render(content,request))

def detail(request, pk):
    try:
        p = Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        raise Http404("poll does not exist")
    return render(request,'polls/detail.html',{'question': p})


def results(request, question_id):
    question = get_object_or_404(Question,pk = question_id)
    return render(request,'polls/results.html',{'question' : question})


def vote(request,question_id):
    question = get_object_or_404(Question,pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):

        return render(request,'polls/detail.html',{
        'question' : question,
        'error_message' : "You did'nt select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return  HttpResponseRedirect(reverse('polls:results',args =(question.id,)))


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'listx'
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'