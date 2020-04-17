from django import forms
from .models import Inventory

class newInventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = "__all__"