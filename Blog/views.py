from django.http import JsonResponse
from django.shortcuts import render,redirect
from .models import Post,Category,Comment,Like
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic.base import View


def poost(request):

    post=Post.objects.all()
    pagenumber=request.GET.get("page")
    article = Paginator(post, 1)

    try:
        art=article.page(pagenumber)
    except PageNotAnInteger:
        art=article.page(1)
    except EmptyPage:
        art=article.page(1)

    return render(request,"Blog/blog.html",{'post':art})


def detail(request,slug):
    like=False

    if request.user.like.filter(articl__slug=slug,user_id=request.user.id):
        like=True
    else:
        like=False

    post=Post.objects.get(slug=slug)
    if request.method=="POST":
         comment=request.POST.get("comment")
         parent=request.POST.get("parent_id")

         Comment.objects.create(body=comment,articl=post,user=request.user,parent_id=parent)



    return render(request,"Blog/post_details.html",context={"post":post,"like":like})


def category_article(request,id):

    category=Category.objects.get(id=id)



    cat=category.post_set.all()


    return render(request,"Blog/article_category.html",{"category":cat})


def search(request):


    q = request.GET.get("q")

    article=Post.objects.filter(titel__icontains=q)

    pagenumber = request.GET.get("page")
    article_set = Paginator(article, 1)
    try:

        art = article_set.page(pagenumber)
    except PageNotAnInteger:
        art = article_set.page(1)
    except EmptyPage:
        art = article_set.page(1)

    return render(request,"Blog/blog.html",{"post":art})


class ListView(View):
    queryset=None
    template_name=None


    def get(self,request):

        return render(request,self.template_name,{"object_list":self.queryset})



class showArticle(ListView):
    queryset = Post.objects.all()
    template_name = "Blog/index.html"


def like(request,slug,pk):

    try:
        like=Like.objects.get(user_id=request.user.id,articl__slug=slug)
        like.delete()
        return JsonResponse({"response": "unlike"})
    except:
        Like.objects.create(user_id=request.user.id,articl_id=pk)
        return JsonResponse({"response":"like"})
