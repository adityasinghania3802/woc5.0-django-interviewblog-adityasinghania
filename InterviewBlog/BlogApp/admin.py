from django.contrib import admin
from BlogApp.models import Account
from BlogApp.models import BlogPost, Comment

admin.site.register(Account)
admin.site.register(BlogPost)
admin.site.register(Comment)