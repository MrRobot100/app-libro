from django.shortcuts import render
from .forms import Correo
from .models import *
from django.contrib.auth.decorators import login_required

def inicio(request):

    try:
        latest_post = Informacion.objects.all().order_by('-fecha')
    except:
        last_update='Error en retirar ultima actualización'

    mail=Correo(request.POST or None)
    if mail.is_valid() and request.method=='POST':
        correo=mail.cleaned_data['correo']
        nombre=mail.cleaned_data['nombre']
        apellido=mail.cleaned_data['apellido']
        nuevo_usuario=Usuarios(nombre=nombre, apellido=apellido, correo=correo)
        nuevo_usuario.save()
        indicador=True
        respuesta={
            'indicador':True,
            'act':latest_post,
        }
        return render(request, 'inicio.html', respuesta)

    respuesta={
        'form':mail,
        'act':latest_post,
    }
    return render(request, 'inicio.html', respuesta)

def about(request):
    respuesta={'about':'no hay información adicional'}
    try:
        about=Front.objects.get(titulo__exact="about")
        respuesta={'about':about.informacion_adicional}
        return render(request,'about.html', respuesta)
    except:
        return render(request,'about.html', respuesta)

#@login_required(login_url='/accounts/login/')
#def tutorial(request):

    #tutorial aqui

#    return render(request,'tutorial.html',respuesta)
