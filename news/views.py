﻿from urllib.request import Request
from django.shortcuts import render
from django.http import HttpResponse
from .models import News, Category

def index(request):
	news = News.objects.all()
	context = {
		'news': news, 
		'title': 'Список новостей',
	}
	return render(request, template_name='news/index.html', context=context)

def get_category(request, category_id):
	news = News.objects.filter(category_id=category_id)
	category = Category.objects.get(pk=category_id)
	return render(request, 'news/category.html', {'news': news, 'category':category})


#	res='<h1>Список новостей</h1>'
#	for item in news:
#		res += f'<div>\n<p>{item.title}</p>\n<p>{item.content}</p>\n</div>\n<hr>'
#	return HttpResponse(res)