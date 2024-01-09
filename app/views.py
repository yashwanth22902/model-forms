from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse

# Create your views here.
def insert_topic(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}
    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            TFDO.save()
            return HttpResponse('insert_topic data is submitted succesfully')

    return render(request,'insert_topic.html',d)



def insert_webpage(request):
    EWFO=WebpageForm()
    d1={'EWFO':EWFO}
    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            WFDO.save()
            return HttpResponse('insert_webpage data is inserted successfully')
    return render(request,'insert_webpage.html',d1)


def insert_AcessRecord(request):
    EARFO=AcessRecordForm()
    d2={'EARFO':EARFO}
    if request.method=='POST':
        ARFDO=AcessRecordForm(request.POST)
        if ARFDO.is_valid():
            ARFDO.save()
            return HttpResponse('insert_AcessRecord data is succesfully done')
    return render(request,'insert_AcessRecord.html',d2)