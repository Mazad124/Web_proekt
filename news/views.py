from urllib.request import Request
from django.shortcuts import render
from django.http import HttpResponse
from .models import News

def index(request):
	news = News.objects.all()
	context = {
		'news': news, 
		'title': 'Список новостей'
	}
	return render(request, template_name='news/index.html', context=context)


#	res='<h1>Список новостей</h1>'
#	for item in news:
#		res += f'<div>\n<p>{item.title}</p>\n<p>{item.content}</p>\n</div>\n<hr>'
#	return HttpResponse(res)