from django import forms
from django.contrib.auth import authenticate
from .models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Usuario',
                'class': 'form-control form-control-lg'
            }
        )
    )
    password = forms.CharField(
        label='',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
                'class': 'form-control form-control-lg'
            }
        )
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not authenticate(username=username, password=password):
            raise forms.ValidationError('Los datos de usuario no son correctos')
        
        return self.cleaned_data


class UserRegisterForm(forms.ModelForm):
    
    username = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Usuario',
                'class': 'form-control form-control-lg'
            }
        )
    )

    password1 = forms.CharField(
        #label = 'Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Contraseña',
                'class': 'form-control form-control-lg'
            }
        )
    )

    password2 = forms.CharField(
        #label = 'Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Repetir contraseña',
                'class': 'form-control form-control-lg'
            }
        )
    )

    class Meta:
        
        model = User
        fields = (
            'username',


        )
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Las contraseñas no son iguales')