from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from . form import createUserForm
# Create your views here.

def  register(request):
    if request.method == 'POST':
        form  = createUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user-login')
    else:
        form = createUserForm()
    context = {'form': form,}
    return render(request, 'user_template/register.html', context)


def userProfile(request):
    return render(request, 'user_template/profile.html')