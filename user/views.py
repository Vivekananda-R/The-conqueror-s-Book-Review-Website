from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import views as authviews


# Create your views here.
def register(requests):

    if requests.method == 'POST':
        form = UserCreationForm(requests.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            # email = form.cleaned_data.get('email')
            messages.success(requests,f'{username} your Account is Created!!')
            form.save()
            return redirect('login')

    else:
        form = UserCreationForm()

    return render(requests,'user/register.html',{'form':form})
