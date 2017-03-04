from django.contrib import admin

from .models import Post, Quote, Project

admin.site.register(Post)
admin.site.register(Quote)
admin.site.register(Project)
