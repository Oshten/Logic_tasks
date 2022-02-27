from django.shortcuts import render, redirect
from django import views

from equation_roots import forms
from equation_roots import models
from equation_roots import functions


class EquationView(views.View):
    """Представление формы коэффициентов уравнения"""

    def get(self, request):
        equation_form = forms.EquationForm
        return render(request, 'equation_roots/equation.html', context={'equation_form': equation_form})

    def post(self, request):
        equation_form = forms.EquationForm(request.POST)
        if equation_form.is_valid():
            equation = models.Equation(**equation_form.cleaned_data)
            equation.save()
            decision = functions.solution_of_equation(**equation_form.cleaned_data)
            solution = models.Solution(solution_x_1=decision['x_1'], solution_x_2=decision['x_2'], equation=equation)
            solution.save()
            return redirect(f'/equation/{equation.solution.id}/solution')
        elif (
                'Equation with this Коэффициент а, Коэффициент b and Коэффициент с already exists.' in equation_form.errors['__all__']
        ):
            equation = models.Equation.objects.get(**equation_form.cleaned_data)

            if not models.Solution.objects.get(equation=equation):
                decision = functions.solution_of_equation(**equation_form.cleaned_data)
                solution = models.Solution(solution_x_1=decision['x_1'], solution_x_2=decision['x_2'],
                                           equation=equation)
                solution.save()
            return redirect(f'/equation/{equation.solution.id}/solution')
        return render(request, 'equation_roots/equation.html', context={'equation_form': equation_form})


class SolutionView(views.View):
    """Представление корней квадратного уравнения"""
    def get(self, request, pk):
        solution = models.Solution.objects.get(id=pk)
        equation = models.Equation.objects.get(solution=solution)
        return render(request, 'equation_roots/solution.html', context={'equation': equation, 'solution': solution})



