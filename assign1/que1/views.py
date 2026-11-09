from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime

def displaytime (currenttime):
    date=datetime.datetime.now()
    msg="<h1>hello everyone</h1>"
    msg+="<h2> current time :" + str(date) + "</h2>"
    h=int(date.strftime('%H'))
    if h<12 :
        msg+="<h2>good morning </h2>"
    elif h<=16 :
        msg+="<h2>good afternoon </h2>"
    elif h<21 :
        msg+="<h2>good evening </h2>"
    else :
        msg+="<h2>good night </h2>"

    return HttpResponse(msg)

