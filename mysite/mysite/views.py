from django.http import HttpResponse


def index(request):
    return HttpResponse("hello, you're looking my website")
