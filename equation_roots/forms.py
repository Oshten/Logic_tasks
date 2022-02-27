from django.forms import ModelForm

from equation_roots import models


class EquationForm(ModelForm):
    """Модель формы"""
    class Meta:
        model = models.Equation
        fields = '__all__'
