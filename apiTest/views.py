from django.shortcuts import render
import requests
from django.http import HttpResponse

# Create your views here.

def test(request):
    response=requests.get('https://api-tokyochallenge.odpt.org/api/v4/odpt:PassengerSurvey?acl:consumerKey=3d673da4a2bc38c165062f42db9fc7d0d02e884d101a6072450cb3e89e48f9f3').json()
    return render(request,'apiTest/test.html',{'response':response})


def index(request):
    if request.method=='GET':
        return render(request, 'apiTest/index.html')
    elif request.method=="POST":
        title=request.POST['title']
        text=request.POST['text']
        return HttpResponse(f'Title : {title}, Text : {text}')