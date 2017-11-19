"""django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from blog.views import index, post_list, post_detail, about, register, archives,\
	category, tag, user_category, user_archives, user_tag, content, user_content,\
	diaries, user_diaries
from blog.feeds import AllPostsRssFeed
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	url(r'^register/$', register, name='register-url'),
	url(r'^$', index, name='index-url'),
	url(r'^diaries/$', diaries, name='diaries-url'),
	url(r'^(?P<username>\w+)/diaries/$', user_diaries, name='user_diaries-url'),
	url(r'^post/$', post_list, name='posts-url'),
	url(r'^post/(\d+)/$', post_detail, name='post-url'),
	url(r'^about/(?P<username>\w+)/$', about, name='about-url'),
	url(r'^content/$', content, name='content-url'),
	url(r'^(?P<username>\w+)/content/$', user_content, name='user_content-url'),
	url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', archives, name='archives-url'),
	url(r'^(?P<username>\w+)/archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', user_archives, name='user_archives-url'),
	url(r'^category/(?P<category_id>[0-9]+)/$', category, name='category-url'),
	url(r'^(?P<username>\w+)/category/(?P<category_id>[0-9]+)/$', user_category, name='user_category-url'),
	url(r'^tag/(?P<tag_id>[0-9]+)/$', tag, name='tag-url'),
	url(r'^(?P<username>\w+)/tag/(?P<tag_id>[0-9]+)/$', user_tag, name='user_tag-url'),
	#url(r'^search/$', search, name='search-url'),
	url(r'^search/$', include('haystack.urls')),
	url(r'^all/rss/$', AllPostsRssFeed(), name='rss'),
	url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', include('django.contrib.auth.urls')),
	
	
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)