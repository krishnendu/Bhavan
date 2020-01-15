from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import user
from django.forms.widgets import *



class UserForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder' : 'Enter First Name'}), label='First Name', max_length=30 )
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input' , 'placeholder' : 'Enter Last Name'}),label='Last Name', max_length=30 )
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'col-md-3 mb-3', 'placeholder' : 'Enter Email Id'}),label='Email Id')
    country_code = forms.CharField(widget=forms.TextInput(attrs={'class': 'col-auto', 'placeholder' : '+91'}),label='Country Code', max_length=5 , required=False)
    phone_number= forms.CharField(widget=forms.NumberInput(attrs={'class': 'input', 'placeholder' : 'Enter Phone Number'}), label='Phone Number')
    dob = forms.DateField(widget=DateInput(attrs={'type' : 'date'}),label='Date of Birth')
    sex=forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder' : 'Enter Sex'}), label='Sex', max_length=10 )
    bio = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'  , 'placeholder' : 'Enter Bio'} ),label='Bio' , required=False )
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control' , 'placeholder' : 'Enter Address'}),label='Full Address' )
    pincode= forms.CharField(widget=forms.NumberInput(attrs={'class': 'col-auto', 'placeholder' : 'Enter Pincode'}))
    image=forms.ImageField(label='Submit Profile Picture'  )

    
    class Meta:
        model = user
        fields = ('first_name','last_name','email','country_code','phone_number','dob'
        ,'sex','bio','address','pincode','image')
