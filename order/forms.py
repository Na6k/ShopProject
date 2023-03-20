from django import forms


CHOICES_Q = [(i, str(i)) for i in range(1, 11)]


class CartAddForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=CHOICES_Q, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
