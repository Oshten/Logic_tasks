from django.db import models


class Equation(models.Model):
    """Модель уравнения a∙x^2 + b∙x + c = 0"""
    coefficient_а = models.FloatField(verbose_name='Коэффициент а')
    coefficient_b = models.FloatField(verbose_name='Коэффициент b')
    coefficient_c = models.FloatField(verbose_name='Коэффициент с')

    def __str__(self):
        return f'{self.coefficient_а}∙x^2 + {self.coefficient_b}∙x + {self.coefficient_c} = 0'

    class Meta:
        unique_together = ['coefficient_а', 'coefficient_b', 'coefficient_c']


class Solution(models.Model):
    """Модель решения уравнения a∙x^2 + b∙x + c = 0"""
    solution_x_1 = models.CharField(max_length=10)
    solution_x_2 = models.CharField(max_length=10)
    equation = models.OneToOneField(Equation, on_delete=models.CASCADE)

    def __str__(self):
        return f'x_1 = {self.solution_x_1}, x_2 = {self.solution_x_2}'


