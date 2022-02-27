from django.shortcuts import render, redirect
from django import views

from guess_color import forms
from guess_color import functions


class ItemNumberView(views.View):
    """Представление для форммы ввода номера предмета"""
    def get(self, request):
        item_number_form = forms.ItemNumberForm
        return render(request, 'guess_color/color.html', context={'item_number_form': item_number_form})

    def post(self, request):
        item_number_form = forms.ItemNumberForm(request.POST)
        if item_number_form.is_valid():
            index = item_number_form.cleaned_data['item_number']
            return redirect(to=f'{index}/')
        return render(request, 'guess_color/color.html', context={'item_number_form': item_number_form})

class ItemColorViev(views.View):
    def get(self, request, pk):
        items = functions.make_items()
        item = items[pk]
        return render(request, 'guess_color/ansver.html', context={'item': item})
