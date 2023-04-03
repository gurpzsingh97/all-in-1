from django.shortcuts import render, redirect, reverse
from .models import Girl, Boy
# Create your views here.

def index(request):

    if request.method == 'POST':
        print("heloooooooooooooooooooooooooooooooooo")
        gender = request.POST.get('gender')
        if gender == 'girl':
            attendingcheck = request.POST.get('attending', False)
            if attendingcheck  == "yes":
                boolVal = True
            else:
                boolVal = False
            girl = Girl.objects.create(
                name=request.POST.get('name'),
                email=request.POST.get('email'),
                attending = boolVal,
                song_request=request.POST.get('song_request', ''),
            )
            girl.save()
        elif gender == 'boy':
            attendingcheck = request.POST.get('attending', False)
            if attendingcheck  == "yes":
                boolVal = True
            else:
                boolVal = False
            boy = Boy.objects.create(
                name=request.POST.get('name'),
                email=request.POST.get('email'),
                attending = boolVal,
                song_request=request.POST.get('song_request', ''),
            )
            boy.save()
        return redirect(reverse('home'))
    else:
        return render(request, 'home/index.html')


    