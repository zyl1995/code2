from django.shortcuts import render, get_object_or_404
from polls.models import Question, Choice
from django.http import HttpResponse, Http404
from  django.template import  RequestContext, loader

def index(request):
    question_list = Question.objects.order_by('-publish_data')[:5]
    # output = ','.join([p.question_text for p in question_list])
    # return HttpResponse(output)
    # template = loader.get_template('polls/index.html')
    # context = RequestContext(request,{
    #     'question_list':question_list,
    # })
    # return HttpResponse(template.render(context))
    context = {'question_list':question_list}
    return render(request, 'polls/index.html', context)

# Create your views here.

def detail(request, question_id):
    # try:
    #question = Question.objects.get(pk=question_id)
    question = get_object_or_404(Question, pk=question_id)
    # except Question.DoesNotExist:
    #     raise  Http404("Question does not exist")
    return render(request,'polls/detail.html',{'question':question})
    # return HttpResponse("You're looking at question %s." %question_id)

def results(request, question_id):
    response = "You're looking at resluts of question %s."
    return HttpResponse(response %question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)