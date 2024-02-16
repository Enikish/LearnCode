from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic

from .models import Question, Choice
from django.template import loader
from django.http import Http404
from django.utils import timezone


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        # 返回最近5个发布的question
        # return Question.objects.order_by("-pub_date")[:5]
        """
        return the last five published questions (not including those set to be published in the future)
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


# Create your views here.
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")


def recall(request):
    return HttpResponse("Hello, you're calling this function")


# def blanc(request):
#     return HttpResponse("<h2>hello</h2>")


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})
    # return HttpResponse("You're looking at question %s " % question_id)


def results(request, question_id):
    # response = "You're looking at the result of question %s."
    # return HttpResponse(response % question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})


def vote(request, question_id):
    # return HttpResponse("You're voting on question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except(KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice."
            }
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # template = loader.get_template("polls/results.html")
        context = {
            "question.id": question.id,
        }
        # 为防止用户点击回退按钮的情况下数据被post两次，所以每次处理完成POST数据后，都需要返回一个HttpResponseRedirect
        return HttpResponse(reverse("polls:results", args=(question.id,)))


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))
