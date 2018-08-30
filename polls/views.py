from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404

from django.template import loader

from .models import Question

def index(request):
    #speju cia imam  penkis paskutinius surusiuotus pagal data
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    #template = loader.get_template('polls/index.html')
    context = {'key_of_question_list': latest_question_list,  }
    #return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Exception as e:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'key_of_question' : question, 'key_of_id' :question_id })

def results(request, question_id):
    response = "You're looking at the result of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s" % question_id)
