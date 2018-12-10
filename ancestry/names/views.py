
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('test')


def about(request):
    return HttpResponse('Here is the about page + <a href="../">home page</a>')

def <view name>(request):
    pass
    # context = {<name-value pairs>}
    # return render(request, '<app name>/<template name>.html', context)