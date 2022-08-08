from django import forms
from django.contrib.auth import authenticate
#from django.forms import ValidationError
from django.core.validators import ValidationError
from django.contrib.auth.models import User

class LoginForm(forms.Form):

    username=forms.CharField(max_length=50,widget=forms.TextInput(attrs={"class":"input100","placeholder":"Enter Your Username"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"input100","placeholder":"Enter Your Password"}))


    def clean_username(self):



        user=User.objects.filter(username=self.cleaned_data.get("username"))

        if user.exists():

            return self.cleaned_data.get("username")

        else:

            raise ValidationError("Username is Not Exist")

    def clean_password(self):



        user=authenticate(username=self.cleaned_data.get("username"),password=self.cleaned_data.get("password"))

        if user is not None:

            return self.cleaned_data.get("password")

        else:
            raise ValidationError("Password Is Not Correct")

class EditForm(forms.ModelForm):

    class Meta:
        model=User
        fields=("first_name","last_name","email","username")
        widgets={
            "first_name":forms.TextInput(attrs={
                "class":"form-control",
            }),
            "last_name":forms.TextInput(attrs={
                "class":"form-control"}),
            "email":forms.TextInput(attrs={
                "class":"form-control"})


        }
