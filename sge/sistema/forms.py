from django import forms
from sistema.models import Electrodomestico
from sistema.models import HoraCasa


class ElectrodomesticoForm(forms.ModelForm):
    class Meta:
        model = Electrodomestico

        fields = [
            'Nombre',
            'Marca',
            'Modelo',
            'Horas',
            'Consumo',
            'Linea',

        ]
        labels = {
            'Nombre': 'Nombre de electrodomestico',
            'Marca': 'Marca',
            'Modelo': 'Modelo',
            'Horas': 'Tiempo de actividad promedio por dia en minutos',
            'Consumo': 'Consumo en watts',
            'Linea': 'Linea',
        }
        widgets = {
            'Nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'Marca': forms.TextInput(attrs={'class': 'form-control'}),
            'Modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'Horas': forms.TextInput(attrs={'class': 'form-control'}),
            'Consumo': forms.TextInput(attrs={'class': 'form-control'}),
            'Linea': forms.HiddenInput(),
        }



class ElectrodomesticoFormEdit(forms.ModelForm):
    class Meta:
        model = Electrodomestico
        fields = [
            'Nombre',
            'Marca',
            'Modelo',
            'Horas',
            'Consumo',
            'Linea',
            'Activo',

        ]
        labels = {
            'Nombre': 'Nombre de electrodomestico',
            'Marca': 'Marca',
            'Modelo': 'Modelo',
            'Horas': 'Tiempo de actividad promedio por dia en minutos',
            'Consumo': 'Consumo en watts',
            'Linea': 'Linea',
            'Activo': 'Activo'
        }
        widgets = {
            'Nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'Marca': forms.TextInput(attrs={'class': 'form-control'}),
            'Modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'Horas': forms.TextInput(attrs={'class': 'form-control'}),
            'Consumo': forms.TextInput(attrs={'class': 'form-control'}),
            'Linea': forms.HiddenInput(),
            'Activo': forms.CheckboxSelectMultiple().choices,
        }


class LuzForm(forms.ModelForm):
    class Meta:
        model = Electrodomestico

        fields = [
            'Nombre',
            'Marca',
            'Modelo',
            'Horas',
            'Consumo',
            'Linea',

        ]
        labels = {
            'Nombre': 'Nombre de lampara',
            'Marca': 'Marca',
            'Modelo': 'Modelo',
            'Horas': 'Tiempo de actividad promedio por dia en minutos',
            'Consumo': 'Consumo en watts',
            'Linea': 'Linea',
        }
        widgets = {
            'Nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'Marca': forms.HiddenInput(),
            'Modelo': forms.HiddenInput(),
            'Horas': forms.HiddenInput(),
            'Consumo': forms.TextInput(attrs={'class': 'form-control'}),
            'Linea': forms.HiddenInput(),
        }

class LuzFormEdit(forms.ModelForm):
    class Meta:
        model = Electrodomestico

        fields = [
            'Nombre',
            'Marca',
            'Modelo',
            'Horas',
            'Consumo',
            'Linea',
            'Activo',

        ]
        labels = {
            'Nombre': 'Nombre de lampara',
            'Marca': 'Marca',
            'Modelo': 'Modelo',
            'Horas': 'Tiempo de actividad promedio por dia en minutos',
            'Consumo': 'Consumo en watts',
            'Linea': 'Linea',
            'Activo': 'Activo',
        }
        widgets = {
            'Nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'Marca': forms.HiddenInput(),
            'Modelo': forms.HiddenInput(),
            'Horas': forms.HiddenInput(),
            'Consumo': forms.TextInput(attrs={'class': 'form-control'}),
            'Linea': forms.HiddenInput(),
            'Activo': forms.CheckboxSelectMultiple().choices,
        }


class ClimatizadorForm(forms.ModelForm):
    class Meta:
        model = Electrodomestico

        fields = [
            'TipoClima',
            'Nombre',
            'Marca',
            'Modelo',
            'Horas',
            'Consumo',
            'Linea',

        ]
        labels = {
            'TipoClima': 'Tipo de CLimatizador',
            'Nombre': 'Nombre de climatizador',
            'Marca': 'Marca',
            'Modelo': 'Modelo',
            'Horas': 'Tiempo de actividad promedio por dia en minutos',
            'Consumo': 'Consumo en watts',
            'Linea': 'Linea',
        }
        widgets = {
            'TipoClima': forms.CheckboxSelectMultiple().choices,
            'Nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'Marca': forms.TextInput(attrs={'class': 'form-control'}),
            'Modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'Horas': forms.HiddenInput(),
            'Consumo': forms.TextInput(attrs={'class': 'form-control'}),
            'Linea': forms.HiddenInput(),
        }

class ClimaFormEdit(forms.ModelForm):
    class Meta:
        model = Electrodomestico

        fields = [
            'TipoClima',
            'Nombre',
            'Marca',
            'Modelo',
            'Horas',
            'Consumo',
            'Linea',
            'Activo',

        ]
        labels = {
            'TipoClima': 'Tipo de CLimatizador',
            'Nombre': 'Nombre de climatizador',
            'Marca': 'Marca',
            'Modelo': 'Modelo',
            'Horas': 'Tiempo de actividad promedio por dia en minutos',
            'Consumo': 'Consumo en watts',
            'Linea': 'Linea',
            'Activo': 'Activo',
        }
        widgets = {
            'TipoClima': forms.CheckboxSelectMultiple().choices,
            'Nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'Marca': forms.TextInput(attrs={'class': 'form-control'}),
            'Modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'Horas': forms.HiddenInput(),
            'Consumo': forms.TextInput(attrs={'class': 'form-control'}),
            'Linea': forms.HiddenInput(),
            'Activo': forms.CheckboxSelectMultiple().choices,
        }

class HoraCasaForm(forms.ModelForm):
    class Meta:
        model = HoraCasa

        fields = [
            'Dia',
            'Inicio',
            'Fin',
        ]
        labels = {
            'Dia': 'Dia de la semana',
            'Inicio': 'Hora de inicio de periodo',
            'Fin': 'Hora de fin de periodo',
        }
        OPTIONS = (
            ("a", "A"),
            ("b", "B"),
        )

    widgets = {
            'Dia': forms.CheckboxSelectMultiple().choices,
            'Inicio': forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
            'Fin': forms.TimeInput(),
        }