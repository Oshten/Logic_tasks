from django import forms

class ItemNumberForm(forms.Form):
    """Форма для номера предмета"""
    item_number = forms.IntegerField(min_value=1, max_value=100)