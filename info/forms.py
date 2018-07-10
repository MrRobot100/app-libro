from django import forms

class Correo(forms.Form):
    correo = forms.EmailField(label='user_mail', required=True)
    nombre = forms.CharField(label='nombre', max_length=200, required=True)
    apellido = forms.CharField(label='nombre', max_length=200, required=True)
