from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import GroomSide, BrideSide
# Create your views here.

def index(request):
    if request.method == "POST":
        if request.POST["side"] == "groomSide":
            groomside = GroomSide()
            groomside.name = request.POST["name"]
            groomside.attending_gurdwara_groom = request.POST["attending_gurdwara_groom"]
            groomside.total_attending_gurdwara_groom = int(request.POST["total_attending_gurdwara_groom"] or 0)
            groomside.coach_attending_gurdwara_groom = int(request.POST["coach_attending_gurdwara_groom"] or 0)
            groomside.attending_reception_groom = request.POST["attending_reception_groom"]
            groomside.total_attending_reception_groom = int(request.POST["total_attending_reception_groom"] or 0)
            groomside.coach_attending_reception_groom = int(request.POST["coach_attending_reception_groom"] or 0)
            groomside.song_request_groom = request.POST["song_request_groom"]
            groomside.save()
            if request.POST["attending_gurdwara_groom"] == 'yes' or request.POST["attending_reception_groom"] == 'yes':
                messages.success(request, "Looking forward to seeing you!")
            else:
                messages.success(request, "Thank you for considering our invitation.")
            return redirect(reverse('home'))
        if request.POST["side"] == "brideSide":
            brideside = BrideSide()
            brideside.name = request.POST["name"]
            brideside.attending_gurdwara_bride = request.POST["attending_gurdwara_bride"]
            brideside.total_attending_gurdwara_bride = int(request.POST["total_attending_gurdwara_bride"] or 0)
            brideside.attending_reception_bride = request.POST["attending_reception_bride"]
            brideside.total_attending_reception_bride = int(request.POST["total_attending_reception_bride"] or 0)
            brideside.song_request_bride = request.POST["song_request_bride"]
            brideside.save()
            if request.POST["attending_gurdwara_bride"] == 'yes' or request.POST["attending_reception_bride"] == 'yes':
                messages.success(request, "Looking forward to seeing you!")
            else:
                messages.success(request, "Thank you for considering our invitation.")
            return redirect(reverse('home'))
            
    return render(request, 'home/index.html')
