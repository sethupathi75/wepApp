from  django import forms
from computerstore.models import computerstore

class store(forms.ModelForm):
    class Meta:
        model=computerstore
        fields='__all__'