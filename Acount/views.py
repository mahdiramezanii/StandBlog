from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from.forms import LoginForm,EditForm


def user_login(request):
    if request.user.is_authenticated==True:
        return redirect("Home:Home")


    if request.method=="POST":

        form=LoginForm(data=request.POST)

        if form.is_valid():
            user=User.objects.get(username=form.cleaned_data.get("username"))
            login(request,user)
            return redirect("Home:Home")

    form=LoginForm()

    return render(request,"Acount/login.html",{"form":form})



def user_register(request):

    context={
        "erors":[]
    }

    if request.user.is_authenticated:
        return redirect("Home:Home")

    if request.method=="POST":

        username=request.POST.get("username")
        email=request.POST.get("email")
        password1=request.POST.get("password1")
        password2=request.POST.get("password2")

        if User.objects.filter(username=username).exists():
            context["erors"].append("نام کاربری از قبل وجود دارد!")

        elif User.objects.filter(email=email).exists():
            context["erors"].append("ایمیل تکراری است!")

        elif password1 != password2:
            context["erors"].append("رمز ها شباهت ندارد!")

        else:
            u=User.objects.create(username=username,password=password1,email=email)
            u.set_password(password1)
            u.save()
            login(request,u)
            return redirect("Home:Home")



    return render(request,"Acount/register.html",context=context)



def edit_user(request):
    user=request.user
    form=EditForm(instance=user)

    if request.method=="POST":
        form=EditForm(instance=user,data=request.POST)

        if form.is_valid():
            form.save()

    return render(request,"Acount/edit.html",{"form":form})


def user_logout(request):

    logout(request)


    return redirect("Home:Home")