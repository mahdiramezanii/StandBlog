from django.urls import path
from . import views

app_name="Blog"
urlpatterns=[
    path("",views.poost,name="Blog"),
    path("detail/<slug:slug>",views.detail,name="detail"),
    path("category/<int:id>",views.category_article,name="catehory_detail"),
    path("view/",views.search,name="search"),
    path("test",views.showArticle.as_view(),name="test"),
    path("like/<slug:slug>/<int:pk>",views.like,name="like"),
]