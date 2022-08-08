from django.shortcuts import render
from Blog.models import Post
def Home(request):

    post=Post.objects.published()
    recent_article=Post.objects.all()[:3]



    return render(request,"Home_app/index.html",{"post":post,"recent_article":recent_article})


def recent(request):

    recentt=Post.objects.all()[:3]





    return render(request,"include/sidebar.html",{"recent":recentt})
