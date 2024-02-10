from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
class InicioSesionView(View):
    template_name = 'inicio_sesion.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Bienvenido, {username}. Has iniciado sesión con éxito.")
            return redirect('index')
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
            return render(request, self.template_name, {'username': username})
class RegistarView(View):
    template_name = 'registro_usuario.html'
    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request): 
        try:
            username = request.POST['username']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            if password1 == password2:
                user = User.objects.create_user(
                    username=username,
                    password=password1,
                    first_name=first_name,
                    last_name=last_name,
                    email=email
                )

                return redirect('Inicio_sesion') 
            else:
                return render(request, 'registro_usuario.html', {'error': 'Las contraseñas no coinciden'})
        except Exception as e:
            return render(request, 'registro_usuario.html', {'error': str(e)})

