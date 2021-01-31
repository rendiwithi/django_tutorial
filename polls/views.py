from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Question

# Create your views here.
# def index(request):
#     return HttpResponse("Hai")
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # VERSI 1
    # template = loader.get_template('polls/index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))
    
    # VERSI 2
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)
    

def detail(request, question_id):
    return HttpResponse("You're Looking at question %s" %question_id)

def results(request, question_id):
    response = "You're Looking at the results of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s" % question_id)

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except:
        # raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})