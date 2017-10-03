from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
	username = models.CharField('用户名', max_length=20, null=False)
	email = models.EmailField()
	password = models.CharField('密  码', max_length=20, null=False)
	
	def __unicode__(self):
		return self.username

class Post(models.Model):
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField('标题', max_length=200)
	body = models.TextField('内容')
	create_time = models.DateTimeField('发布日期', default=timezone.now)
	update_time = models.DateTimeField('最后修改日期', auto_now = True)
	
	class Meta:
		ordering = ('-create_time',)
	
	def __unicode__(self):
		return self.title