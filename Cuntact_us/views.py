from django.shortcuts import render
from .forms import Contactforms
from .models import Message

def contact(request):

    if request.method=="POST":
        form=Contactforms(data=request.POST)

        if form.is_valid():
            titel=form.cleaned_data.get("titel")
            text=form.cleaned_data.get("text")
            email=form.cleaned_data.get("email")
            Message.objects.create(titel=titel,text=text,email=email)
    else:
        form = Contactforms()

    return render(request,"Cuntact_us/contact.html",{"form":form})
