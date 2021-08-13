from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from sisdemo.forms import RegisterForm

from django.contrib.auth import authenticate, login, logout


# Create your views here.



def index(request):


    return render(request, 'index.html')


def panel(request):

    return render(request, 'panel/panel.html',{'title': 'Home'})


"""""
def register(request):

    return render(request, 'registro/registro.html',{'title': 'Registro'})

"""



def register(request):


    if request.user.is_authenticated:
        return redirect('panel')
    else:

        register_form = RegisterForm()

        if request.method == 'POST':
            register_form = RegisterForm(request.POST)

            if register_form.is_valid():
                register_form.save()

                # CREAR MENSAJE FLASH
                messages.success(request, 'Te haz registado correctamente!')


                return redirect('register')


        return render(request, 'registro/registro.html',{
            'title': 'Registro',
            'form': register_form

        })


def login_user(request):

     if request.user.is_authenticated:
        return redirect('panel')
     else:

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                return redirect('panel')

            else:
                messages.warning(request, 'Error ingresar correctamente tus credenciales!')



        return render(request, 'index.html')



def logout_user(request):
    logout(request)

    return redirect('index')




