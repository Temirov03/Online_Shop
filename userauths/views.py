from django.shortcuts import render,redirect
from userauths.forms import UserRegisterForm
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from django.conf import settings
from userauths.models import User

# User = settings.AUTH_USER_MODEL


def register_view(request):
    form = UserRegisterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"Hey {username}, Your accounts was created success")
            new_user = authenticate(username=form.cleaned_data['email'],
                                    password = form.cleaned_data['password1']
            )

            login(request, new_user)
            return redirect('core:index')

    else:
        print('AAALLIIIIII')
    
    context = {
        'form': form,   
    }
    return render(request,'userauths/sign-up.html', context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect('core:index')
    
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        

        try:
            user =User.objects.get(email=email)

            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request,user)
                messages.success(request,"You are logged in.")
                return redirect('core:index')
            else:
                messages.warning(request,'User does not Exist. Create an account.')
        except:
            messages.warning(request,f'User with {email} does not exist')


    return render(request, "userauths/sign-in.html")


def logout_view(request):
    logout(request)
    messages.success(request,"You logged out.")
    return redirect("userauths:sign-in")
