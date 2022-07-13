from django import forms
from .models import MyUser


class CreateUserForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = "__all__"
