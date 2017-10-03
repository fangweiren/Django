from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template.loader import get_template
from .models import User, Post

# Create your views here.
def index(request):
	template = get_template('index.html')
	try:
		posts = Post.objects.all()
	except:
		pass
	html = template.render(locals())
	return HttpResponse(html)
	#return render(request, 'index.html')
	
def post(request):
	template = get_template('index.html')
	try:
		posts = Post.objects.all()
	except:
		pass
	html = template.render(locals())
	return HttpResponse(html)
	
def post1(request, post_id):
	template = get_template('post.html')
	try:
		post = Post.objects.get(id=post_id)
	except Post.DoesNotExist:
		raise Http404('找不到指定的文章')
	html = template.render(locals())
	return HttpResponse(html)