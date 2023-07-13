from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Veterinario, Mascota, Propietario


class VeterinarioForm(forms.ModelForm):
    class Meta:
        model = Veterinario
        fields = ['nombre', 'especialidad', 'telefono']

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre', 'especie', 'edad', 'propietario']

class PropietarioForm(forms.ModelForm):
    class Meta:
        model = Propietario
        fields = ['nombre', 'direccion', 'telefono']
        
    
class BusquedaForm(forms.Form):
    termino_busqueda = forms.CharField(label='Buscar', max_length=100)

class LoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email')