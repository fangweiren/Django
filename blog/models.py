from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
	SEX = (
		('M', '男'),
		('F', '女'),
	)
	user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='用户名')
	user_avatar = models.ImageField('头像' ,upload_to='avatar', default='BX3.jpg')
	sex = models.CharField('性别',max_length=1, choices=SEX)
	birthday = models.DateTimeField('出生年月', blank=True)
	register_DateTime = models.DateTimeField('注册日期', blank=True)
	login_DateTime = models.DateTimeField('最后登录日期', blank=True)
	
	class Meta:
		verbose_name = '个人资料'
		verbose_name_plural = "个人资料"
	
	def __str__(self):
		return self.user.username
		
class Category(models.Model):
	name = models.CharField('分类', max_length=100)
	
	class Meta:
		verbose_name = '分类'
		verbose_name_plural = "分类"
	
	def __str__(self):
		return self.name
		
class Tag(models.Model):
	name = models.CharField('标签', max_length=100)
	
	class Meta:
		verbose_name = '标签'
		verbose_name_plural = "标签"
	
	def __str__(self):
		return self.name

class Post(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户名')
	title = models.CharField('标题', max_length=100)
	body = models.TextField('内容')
	create_time = models.DateTimeField('发布日期', default=timezone.now)
	update_time = models.DateTimeField('最后修改日期', auto_now=True)
	read_amount = models.IntegerField('浏览', default=0)
	category = models.ForeignKey(Category, blank=True, verbose_name='分类')
	tags = models.ManyToManyField(Tag, blank=True, verbose_name='标签')
	
	class Meta:
		ordering = ('-create_time',)
		verbose_name = '博客'
		verbose_name_plural = "博客"
		
	def yueduliang(self):
		self.read_amount += 1
		self.save(update_fields=['read_amount'])
	
	def __str__(self):
		return self.title
		
class Diary(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户名')
	body = models.TextField('日记')
	create_time = models.DateTimeField('发布日期', default=timezone.now)
	
	class Meta:
		ordering = ('-create_time',)
		verbose_name = '日记'
		verbose_name_plural = "日记"
		
	def __str__(self):
		return self.body