from django.http import HttpResponse

# Hello world test view
def hello(request):
    return HttpResponse("Hello world")
