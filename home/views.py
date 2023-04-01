from django.shortcuts import render
from .models import Girl, Boy
# Create your views here.

def index(request):
    print("heloooooooooooooooooooooooooooooooooo11111111")
    if request.method == 'POST':
        print("heloooooooooooooooooooooooooooooooooo")
        gender = request.POST.get('gender')
        if gender == 'girl':
            girl = Girl.objects.create(
                name=request.POST.get('name'),
                email=request.POST.get('email'),
                attending=request.POST.get('attending', False),
                song_request=request.POST.get('song_request', ''),
            )
            girl.save()
        elif gender == 'boy':
            boy = Boy.objects.create(
                name=request.POST.get('name'),
                email=request.POST.get('email'),
                attending=request.POST.get('attending', False),
                meal_choice=request.POST.get('song_request', ''),
            )
            boy.save()
        return render(request, 'home/index.html')
    else:
        return render(request, 'home/index.html')


    