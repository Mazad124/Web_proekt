﻿from django.urls import path

from .views import *

urlpatterns = [
    path('', HomeNews.as_view(), name='home'),
    #path('', index, name='home'),
    path('category/<int:category_id>/', NewsByCategory.as_view(extra_context = {'title': 'Категории'}), name='category'),
    #path('category/<int:category_id>/', get_category, name='category'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    #path('news/<int:news_id>/', view_news, name='view_news'),
    #path('news/add_news/', add_news, name='add_news'),
    path('news/add_news/', CreateNews.as_view(), name='add_news'),
]

