from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import format_html
from django.utils.text import slugify

class articls(models.Manager):

    def published(self):

        return self.filter(status=True)


class Category(models.Model):

    titel=models.CharField(max_length=50)


    def get_absolut_url(self):

        return reverse("Blog:catehory_detail",kwargs={"id":self.id})

    class Meta:
        verbose_name="دسته بندی"
        verbose_name_plural="دسته بندی ها"

    def __str__(self):
        return self.titel

class Post(models.Model):
    category=models.ManyToManyField(Category)
    auther=models.ForeignKey(User,on_delete=models.CASCADE,)
    titel=models.CharField(max_length=50)
    text=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to="blog/img")
    status=models.BooleanField(default=True)
    slug=models.SlugField(unique=True,blank=True,null=True)
    published=models.BooleanField(default=True)
    objects=articls()


    def show_img(self):

        return format_html(f'<img src="{self.image.url}" width="30px" height="40px">')

    show_img.short_description="عکس ها"

    def show_text(self):

        return self.text[0:150]

    class Meta:
        ordering=["-date"]


    def get_absolout_url(self):

        return reverse("Blog:detail",kwargs={"slug":self.slug})


    def __str__(self):

        return f"{self.titel},{self.auther}"


    def save(self,*args,**kwargs):

        self.slug=slugify(self.titel)

        super(Post,self).save(*args,**kwargs)


    class Meta:
        verbose_name="مقاله"
        verbose_name_plural="مقاله ها"


class Comment(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user")
    articl=models.ForeignKey(Post,on_delete=models.CASCADE,related_name="article")
    parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name="replay")
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.body[:20]

    class Meta:
        verbose_name="کامنت"
        verbose_name_plural="مقاله ها"


class Like(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="like")
    articl=models.ForeignKey(Post,on_delete=models.CASCADE,related_name="like")
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return f"{self.user.username} -> {self.articl.titel}"

    class Meta:
        verbose_name="لایک"
        verbose_name_plural="لایک ها"
