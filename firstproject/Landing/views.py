from django.shortcuts import render
# from django.http import HttpRespons

# Create your views here.
def index(request):
    return render(request,'Landing/index.html')
    # return HttpRespons("HELLO")

def study(request):
    return render(request,'Landing/study.html')

def myblog(request):
    return render(request,'Landing/myblog.html')
