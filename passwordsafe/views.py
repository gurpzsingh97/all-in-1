from django.shortcuts import render, get_object_or_404, reverse, redirect
from .forms import AddpasswordForm
from .models import PasswordSafe
from django.contrib import messages

# Create your views here.
def view_passwords(request):
    try:
        sortkey = 'platform_name'
        order = 'asc'
        if 'sort_order' in request.GET:
            order = request.GET['sort_order']
            if order == 'asc':
                sortkey = sortkey
            elif order == 'desc':
                sortkey = f'-{sortkey}'
        safes = PasswordSafe.objects.filter(user=request.user).order_by(sortkey)
    except:
        safes = None
        order = 'asc'

    context = {
        'safes': safes,
        'order': order
    }
    return render(request, 'passwordsafe/passwordsafe.html',context)


def add_password(request):
    form = AddpasswordForm
    if request.method == 'POST':
        password_form = AddpasswordForm(request.POST)
        if password_form.is_valid():
            obj = password_form.save(commit=False)
            obj.user = request.user
            obj.save()
            messages.success(request, 'Item has been added')
            return redirect(reverse('passwordsafe'))
        else:
            messages.error('not working')

    
    try:
        sortkey = 'platform_name'
        order = 'asc'
        if 'sort_order' in request.GET:
            order = request.GET['sort_order']
            if order == 'asc':
                sortkey = sortkey
            elif order == 'desc':
                sortkey = f'-{sortkey}'
        safes = PasswordSafe.objects.filter(user=request.user).order_by(sortkey)
    except:
        safes = None
        order = 'asc'

    context = {
        'form': form,
        'safes':safes,
        'order':order
    }

    return render(request, 'passwordsafe/addpassword.html', context)


def delete_password(request ,item_id):
    try:
        safe = get_object_or_404(PasswordSafe, pk=item_id)
        safe.delete()
        messages.success(request, 'Item has been deleted')
    except:
        messages.error(request, 'failed to delete')


    return redirect(reverse('passwordsafe'))