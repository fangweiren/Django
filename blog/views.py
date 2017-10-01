from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template.loader import get_template

# Create your views here.
def index(request):
	#template = get_template('index.html')
	#html = template.render()
	#return HttpResponse(html)
	#return HttpResponse('hello world!')
	return render(request, 'index.html')
