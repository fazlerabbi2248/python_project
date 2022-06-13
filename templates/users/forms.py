from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import profileModel
from django import forms

class singUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
    def __init__(self, *args, **kwargs):
        super(singUpForm, self).__init__(*args, **kwargs)

        for fieldname in ['username','email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']
    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)

        for fieldname in ['username','email']:
            self.fields[fieldname].help_text = None
class ProfieUpdateForm(forms.ModelForm):
    class Meta:
        model = profileModel
        fields = ['image']

