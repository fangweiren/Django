import markdown
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Profile, Category, Tag, Diary
from django.db.models import Q
from django.core.paginator import PageNotAnInteger, Paginator, InvalidPage, EmptyPage
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
	if request.user.is_authenticated():
		username = request.user.username
		try:
			user = User.objects.get(username=username)
			posts = Post.objects.filter(author=user)
			profile = Profile.objects.get(user=user)			
		except Profile.DoesNotExist:
			#raise Http404('找不到指定的文章')
			pass
	else:
		posts = Post.objects.all()
		
	template = get_template('index.html')
	
	for post in posts:
		post.body = markdown.markdown(post.body,
                                  extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])		
	
	after_range_num = 4
	before_range_num = 4
	try:
		page = int(request.GET.get("page", 1))
		if page < 1:
			page = 1
	except ValueError:
		page = 1
	paginator = Paginator(posts, 15)
	count = paginator.count
	try:
		post_list = paginator.page(page)
		#read_posts = Post.objects.all().order_by('-read_amount')
	except(EmptyPage,InvalidPage,PageNotAnInteger):
		post_list = paginator.page(paginator.num_pages)
	if page >= after_range_num:
		page_range = paginator.page_range[page - after_range_num : page + before_range_num]
	else:
		page_range = paginator.page_range[0 : int(page) + before_range_num]
		
	html = template.render(locals())
	return HttpResponse(html)
	#return render(request, 'index.html')
	
def post_list(request):
	template = get_template('index.html')
	try:
		post_list = Post.objects.all()
		for post in post_list:
			post.body = markdown.markdown(post.body,
                                  extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
	except:
		pass
		
	after_range_num = 4
	before_range_num = 4
	try:
		page = int(request.GET.get("page", 1))
		if page < 1:
			page = 1
	except ValueError:
		page = 1
	paginator = Paginator(post_list, 15)
	count = paginator.count
	try:
		post_list = paginator.page(page)
		#read_posts = Post.objects.all().order_by('-read_amount')
	except(EmptyPage,InvalidPage,PageNotAnInteger):
		post_list = paginator.page(paginator.num_pages)
	if page >= after_range_num:
		page_range = paginator.page_range[page - after_range_num : page + before_range_num]
	else:
		page_range = paginator.page_range[0 : int(page) + before_range_num]
	html = template.render(locals())
	return HttpResponse(html)
	
def post_detail(request, post_id):
	template = get_template('post_detail.html')
	try:
		post = Post.objects.get(id=post_id)
		user = User.objects.get(username=post.author)
		
		post.body = markdown.markdown(post.body,
                                  extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])							  
		post.yueduliang()
	except Post.DoesNotExist:
		raise Http404('找不到指定的文章')
	try:
		profile = Profile.objects.get(user=user)
	except:
		pass
	html = template.render(locals())
	return HttpResponse(html)

def diaries(request):
	template = get_template('diary.html')
	try:
		diary_list = Diary.objects.all()
	except:
		pass
	html = template.render(locals())
	return HttpResponse(html)

def user_diaries(request, username):
	template = get_template('diary.html')
	try:
		user = User.objects.get(username=username)
		diary_list = Diary.objects.filter(author=user)
	except:
		pass
	html = template.render(locals())
	return HttpResponse(html)
	
@login_required(login_url='user/login')
def about(reuqest, username):
	template = get_template('about.html')
	try:
		user = User.objects.get(username=username)
		profile = Profile.objects.get(user=user)			
	except Profile.DoesNotExist:
		pass
	html = template.render(locals())
	return HttpResponse(html)
	
def register(request):
    # 从 get 或者 post 请求中获取 next 参数值
    # get 请求中，next 通过 url 传递，即 /?next=value
    # post 请求中，next 通过表单传递，即 <input type="hidden" name="next" value="{{ next }}"/>
    redirect_to = request.POST.get('next', request.GET.get('next', ''))

    # 只有当请求为 POST 时，才表示用户提交了注册信息
    if request.method == 'POST':
        # request.POST 是一个类字典数据结构，记录了用户提交的注册信息
        # 这里提交的就是用户名（username）、密码（password）、确认密码、邮箱（email）
        # 用这些数据实例化一个用户注册表单
        form = UserCreationForm(request.POST)

        # 验证数据的合法性
        if form.is_valid():
            # 如果提交数据合法，调用表单的 save 方法将用户数据保存到数据库
            form.save()

            if redirect_to:
                return redirect(redirect_to)
            else:
                return redirect('/')
    else:
        # 请求不是 POST，表明用户正在访问注册页面，展示一个空的注册表单给用户
        form = UserCreationForm()

    # 渲染模板
    # 如果用户正在访问注册页面，则渲染的是一个空的注册表单
    # 如果用户通过表单提交注册信息，但是数据验证不合法，则渲染的是一个带有错误信息的表单
    # 将记录用户注册前页面的 redirect_to 传给模板，以维持 next 参数在整个注册流程中的传递
    return render(request, 'users/register.html', context={'form': form, 'next': redirect_to})
	
def archives(request, year, month):
	post_list = Post.objects.filter(create_time__year=year,create_time__month=month).order_by('-create_time')
	
	after_range_num = 4
	before_range_num = 4
	try:
		page = int(request.GET.get("page", 1))
		if page < 1:
			page = 1
	except ValueError:
		page = 1
	paginator = Paginator(post_list, 15)
	count = paginator.count
	try:
		post_list = paginator.page(page)
	except(EmptyPage,InvalidPage,PageNotAnInteger):
		post_list = paginator.page(paginator.num_pages)
	if page >= after_range_num:
		page_range = paginator.page_range[page - after_range_num : page + before_range_num]
	else:
		page_range = paginator.page_range[0 : int(page) + before_range_num]
	return render(request, 'index.html', context={'post_list': post_list, 'page_range': page_range, 'count':count})

#某个分类
def category(request, category_id):
	# 记得在开始部分导入 Category 类
	cate = get_object_or_404(Category, id=category_id)
	post_list = Post.objects.filter(category=cate).order_by('-create_time')
	
	after_range_num = 4
	before_range_num = 4
	try:
		page = int(request.GET.get("page", 1))
		if page < 1:
			page = 1
	except ValueError:
		page = 1
	paginator = Paginator(post_list, 15)
	count = paginator.count
	try:
		post_list = paginator.page(page)
	except(EmptyPage,InvalidPage,PageNotAnInteger):
		post_list = paginator.page(paginator.num_pages)
	if page >= after_range_num:
		page_range = paginator.page_range[page - after_range_num : page + before_range_num]
	else:
		page_range = paginator.page_range[0 : int(page) + before_range_num]
	return render(request, 'index.html', context={'post_list': post_list, 'page_range': page_range, 'count':count})

def user_category(request, username, category_id):
	user = get_object_or_404(User, username=username)
	category = get_object_or_404(Category, id=category_id)
	profile = Profile.objects.get(user=user)
	post_list = Post.objects.filter(category=category, author=user).order_by('-create_time')
	return render(request, 'index.html', context={'post_list': post_list, 'profile': profile})
	
def user_tag(request, username, tag_id):
	user = get_object_or_404(User, username=username)
	tags = get_object_or_404(Tag, id=tag_id)
	profile = Profile.objects.get(user=user)
	post_list = Post.objects.filter(tags=tags, author=user).order_by('-create_time')
	return render(request, 'index.html', context={'post_list': post_list, 'profile': profile})	
	
def user_archives(request, username, year, month):
	user = get_object_or_404(User, username=username)
	profile = Profile.objects.get(user=user)
	post_list = Post.objects.filter(author=user, create_time__year=year,create_time__month=month).order_by('-create_time')
	return render(request, 'index.html', context={'post_list': post_list, 'profile': profile})	
	
def tag(request, tag_id):
	tag = get_object_or_404(Tag, id=tag_id)
	post_list = Post.objects.all().filter(tags=tag)
	
	after_range_num = 4
	before_range_num = 4
	try:
		page = int(request.GET.get("page", 1))
		if page < 1:
			page = 1
	except ValueError:
		page = 1
	paginator = Paginator(post_list, 15)
	count = paginator.count
	try:
		post_list = paginator.page(page)
	except(EmptyPage,InvalidPage,PageNotAnInteger):
		post_list = paginator.page(paginator.num_pages)
	if page >= after_range_num:
		page_range = paginator.page_range[page - after_range_num : page + before_range_num]
	else:
		page_range = paginator.page_range[0 : int(page) + before_range_num]
	return render(request, 'index.html', context={'post_list': post_list, 'page_range': page_range, 'count':count})

#目录视图
def content(request):
	post_list = Post.objects.all()
	
	after_range_num = 4
	before_range_num = 4
	try:
		page = int(request.GET.get("page", 1))
		if page < 1:
			page = 1
	except ValueError:
		page = 1
	paginator = Paginator(post_list, 30)
	count = paginator.count
	try:
		post_list = paginator.page(page)
	except(EmptyPage,InvalidPage,PageNotAnInteger):
		post_list = paginator.page(paginator.num_pages)
	if page >= after_range_num:
		page_range = paginator.page_range[page - after_range_num : page + before_range_num]
	else:
		page_range = paginator.page_range[0 : int(page) + before_range_num]
	context = {
				'post_list': post_list,
				'page_range': page_range, 
				'count':count,
			  }
	return render(request, 'content.html', context=context)
	
def user_content(request, username):
	user = User.objects.get(username=username)
	post_list = Post.objects.filter(author=user)
	
	after_range_num = 4
	before_range_num = 4
	try:
		page = int(request.GET.get("page", 1))
		if page < 1:
			page = 1
	except ValueError:
		page = 1
	paginator = Paginator(post_list, 30)
	count = paginator.count
	try:
		post_list = paginator.page(page)
	except(EmptyPage,InvalidPage,PageNotAnInteger):
		post_list = paginator.page(paginator.num_pages)
	if page >= after_range_num:
		page_range = paginator.page_range[page - after_range_num : page + before_range_num]
	else:
		page_range = paginator.page_range[0 : int(page) + before_range_num]
	context = {
				'post_list': post_list,
				'page_range': page_range, 
				'count':count,
			  }
	return render(request, 'content.html', context=context)
	
'''
# 全文检索与关键词高亮，采用第三方django-haystack
def search(request):
	q = request.GET.get('keyboard')
	error_msg = ''
	
	if not q:
		error_msg = "请输入关键词"
		return render(request, 'index.html', {'error_msg': error_msg})
		
	post_list = Post.objects.filter(Q(title__icontains=q) | Q(body__icontains=q))
	return render(request, 'index.html', {'error_msg': error_msg,
                                               'post_list': post_list})
'''