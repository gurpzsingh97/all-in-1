from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import GroomSide, BrideSide
# Create your views here.

def index(request):
    if request.method == "POST":
        if request.POST["side"] == "groomSide":
            groomside = GroomSide()
            groomside.name = request.POST["name"]
            groomside.attending = request.POST["attending"]
            groomside.total_attending = request.POST["total_attending"]
            groomside.coach_attending = request.POST["coach_attending"]
            groomside.song_request = request.POST["song_request"]
            groomside.save()
            if request.POST["attending"] == 'yes':
                messages.success(request, "Looking forward to seeing you!")
            else:
                messages.success(request, "Thank you for considering our invitation.")
            return redirect(reverse('home'))
        if request.POST["side"] == "brideSide":
            brideside = BrideSide()
            brideside.name = request.POST["name"]
            brideside.attending = request.POST["attending"]
            brideside.total_attending = request.POST["total_attending"]
            brideside.song_request = request.POST["song_request"]
            brideside.save()
            if request.POST["attending"] == 'yes':
                messages.success(request, "Looking forward to seeing you!")
            else:
                messages.success(request, "Thank you for considering our invitation.")
            return redirect(reverse('home'))
            
    return render(request, 'home/index.html')


    