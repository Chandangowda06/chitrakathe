from django.contrib import admin
from .models import Post, Image, Members, Category

# Register your models here.
admin.site.register(Post)
admin.site.register(Image)
admin.site.register(Members)
admin.site.register(Category)