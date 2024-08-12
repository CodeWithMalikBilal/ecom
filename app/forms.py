from django import forms 
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from .models import Customer


class CustomerRegisterForm(UserCreationForm):
    password1 = forms.CharField(label="",widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    password2 = forms.CharField(label="",widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}))
    email = forms.CharField(label="",required=True,widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))
    fullname = forms.CharField(label="" , widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Full Name'}))
    class Meta:
        model = User
        fields = ['username','fullname','email','password1','password2']
        labels = {'username':""}
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Username'})
        
        }
        


class CustomerLoginForm(AuthenticationForm):
    username = UsernameField(label="",widget = forms.TextInput(attrs={'autofocus':True,'placeholder':'Username'}))
    password = forms.CharField(label=_(""),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','placeholder':'Password'}))

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name','email','mobile','address']
        labels = {
            'name':"",
            'email':"",
            'mobile':"",
            'address':"",
        }
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'email':forms.EmailInput(attrs={'class':'form-contrl','placeholder':'Email'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control','placeholder':'Mobile Number'}),
            'address':forms.Textarea(attrs={'class':'form-control' , 'placeholder':'Address'}),
        }