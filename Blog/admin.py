from django.contrib import admin
from .models import Post,Category,Comment,Like

@admin.register(Post)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("__str__","status","show_img")
    list_editable = ("status",)
    list_filter = ("status","published")
    search_fields = ("titel","text")


admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Like)
