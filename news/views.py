from urllib.request import Request
from django.shortcuts import render
from django.http import HttpResponse
from .models import News

def index(request):
	news = News.objects.order_by('-created_at')
	return render(request, 'news/index.html', {'news': news, 'title': 'Список новостей'})


#	res='<h1>Список новостей</h1>'
#	for item in news:
#		res += f'<div>\n<p>{item.title}</p>\n<p>{item.content}</p>\n</div>\n<hr>'
#	return HttpResponse(res)