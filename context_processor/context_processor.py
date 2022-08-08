from Blog.models import Post
from Blog.models import Category


def recent_article(request):

    recent=Post.objects.all()[0:3]
    category=Category.objects.all()

    return {"recent_article":recent,"category":category}