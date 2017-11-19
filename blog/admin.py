from django.contrib import admin
#from django.contrib.auth.models import User
from .models import Post, Category, Tag, Profile, Diary

# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ('author', 'title', 'body', 'read_amount','create_time', 'update_time', 'category', 'tags_list')
	filter_horizontal = ('tags',)
	
	def tags_list(self, post):
		names = map(lambda x: x.name, post.tags.all())
		return ', '.join(names)
	
class UserAdmin(admin.ModelAdmin):
	list_display = ('username', 'email', 'password')
	
class ProfileAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'user_avatar', 'sex', 'birthday', 'register_DateTime', 'login_DateTime')	
	
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')	

class TagAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')
	
class DiaryAdmin(admin.ModelAdmin):
	list_display = ('author', 'body', 'create_time')
	
admin.site.register(Post, PostAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Diary, DiaryAdmin)