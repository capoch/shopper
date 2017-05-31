from django import forms

from .models import Item

from pagedown.widgets import PagedownWidget


class ItemForm(forms.ModelForm):
    due_date = forms.DateField(required=False, widget=forms.SelectDateWidget)
    class Meta:
        model = Item
        fields = ['item_name','description','amount','due_date','image','private']
