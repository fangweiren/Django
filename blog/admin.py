from django.contrib import admin
from .models import User, Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'body','create_time', 'update_time')
	
class UserAdmin(admin.ModelAdmin):
	list_display = ('username', 'email', 'password')

admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)