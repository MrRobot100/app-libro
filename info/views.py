from django.shortcuts import render
from .forms import Correo
from .models import Informacion, Usuarios, Front
from django.contrib.auth.decorators import login_required

def inicio(request):
    """Landing page de la App"""

    try:
        latest_post = Informacion.objects.all().order_by('-fecha')

    except:
        # idenrificar error reprotducido y añadirlo en la captura
        last_update = 'Error en retirar ultima actualización'

    mail = Correo(request.POST or None)

    if mail.is_valid() and request.method == 'POST':

        correo = mail.cleaned_data['correo']
        nombre = mail.cleaned_data['nombre']
        apellido = mail.cleaned_data['apellido']

        nuevo_usuario = Usuarios(nombre=nombre, apellido=apellido, correo=correo)
        nuevo_usuario.save()

        respuesta = {'indicador':True,'act':latest_post}
        return render(request, 'inicio.html', respuesta)

    respuesta = {'form':mail,'act':latest_post}
    return render(request, 'inicio.html', respuesta)

def about(request):
    """About page"""
    
    try:

        about = Front.objects.get(titulo__exact="about")
        respuesta = {'about':about.informacion_adicional}

    except: #identifica el error a capturar

        #loggear el error
        respuesta = {'about':'no hay información adicional'}
        pass

    return render(request,'about.html', respuesta)
