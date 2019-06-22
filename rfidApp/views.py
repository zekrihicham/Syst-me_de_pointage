from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login , logout
from django.http import HttpResponse,JsonResponse
from .models import *
import datetime

import RPi.GPIO as GPIO
import mfrc522.SimpleMFRC522 as SM
import lcddriver
# Create your views here.


def home(request):
    error = ""

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect(users)
        else:
            error = "une error"
            return render(request, 'index.html', locals())

    else:
        return render(request, 'index.html', locals())




def users(request):

    utlisateurs = Utlisateur.objects.all()
    return render(request,'base.html',locals())




def adduser(request):
    GPIO.setmode(GPIO.BOARD)
    reader = SM()
    display = lcddriver.lcd()

    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        try:
            display.lcd_clear() # Write line of text to first line of display

            display.lcd_display_string("Pointez ici !", 1) # Write line of text to first line of display
            
            id,text = reader.read()
        finally:
            GPIO.cleanup()
        rfid=id

        Utlisateur.objects.create(rfid=rfid,first_name=first_name,last_name=last_name)
        return redirect(users)


    else:
        return render(request, 'base2.html', locals())



def sup(request,id):
    Utlisateur.objects.get(pk=id).delete()
    return redirect(users)
    

def logout(request):
    login(request)
    return redirect(home)


def presence(request,id):

    user=Utlisateur.objects.get(id=id)
    presences = Presence.objects.filter(user=user)


    return render(request,'base3.html',locals())



def test (request):
    if request.method == "GET" :
        rfid = request.GET["rfid"]
        try:
            print(rfid)
            user=Utlisateur.objects.get(rfid=rfid)
            print('iiiiii')
            Presence.objects.create(user=user,date=datetime.datetime.now())
            print('kkkkk')
            return HttpResponse("OK")

        except Utlisateur.DoesNotExist:
            user = None
            return HttpResponse("ERR")
        return HttpResponse("hello")
    else:
        return HttpResponse("hello")
