from django import forms
from .models import User


class People(forms.ModelForm):
    error_css_class = "error-field"
    required_css_class = "required-field"
    
    Password= forms.CharField(widget = forms.TextInput(attrs ={"class":"form-control","placeholder":"Password","type": "password"}))
    First_name= forms.CharField(widget = forms.TextInput(attrs ={"class":"form-control","placeholder":"First name"}))
    Last_name= forms.CharField(widget = forms.TextInput(attrs ={"class":"form-control","placeholder":"Last name"}))
    Email= forms.CharField(widget = forms.TextInput(attrs ={"class":"form-control","placeholder":"@gmail.com"}))
    class Meta:
        model = User
        fields =['First_name','Last_name','Email','Password']


class Loginform(forms.Form):
    error_css_class = "error-field"
    required_css_class = "required-field"
    Email = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"@gmail.com","type" : "email"}))
    Password = forms.CharField(widget=forms.TextInput(attrs={"placeholder" : "password","type" : "password"}))

