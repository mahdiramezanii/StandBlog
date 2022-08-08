from django import forms
from django.core.validators import ValidationError
from .models import Message

class testfoorm(forms.Form):
    text=forms.CharField(max_length=10,label="Your Messgae",widget=forms.Textarea(attrs={}))
    name=forms.CharField(max_length=22,label="Name")


    def clean(self):

        name=self.cleaned_data.get("name")
        text=self.cleaned_data.get("text")



        if name == text:
            raise ValidationError("name and text same cant be same",code="name_text_same")



    def clean_name(self):

        name=self.cleaned_data.get("name")

        if "a" in name:

            raise ValidationError("a exisit in name")

        else:

            return name


class Contactforms(forms.ModelForm):

    class Meta:
        model=Message
        fields="__all__" #("titel","text","email",)
        widgets={
            "titel":forms.TextInput(attrs={
                "class":"form-control",
                "placeholder":"Enter Titel"
            }),
            "text":forms.Textarea(attrs={
                "class":"form-control"
            })
        }



