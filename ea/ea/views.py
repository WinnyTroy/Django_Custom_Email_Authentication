from django.http import HttpResponse


def first(request):
    return HttpResponse('Welcome to my site')
