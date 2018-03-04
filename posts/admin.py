from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'created', 'updated')
	list_filter = ('created', 'updated')
	search_fields = ('title', 'text', 'body')


admin.site.register(Post, PostAdmin)