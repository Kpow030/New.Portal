from django.urls import path, re_path
from .views import index, detail, PostCreateView, PostUpdateView, PostDeleteView, CategoryList, subscribe
from django.views.decorators.cache import cache_page



urlpatterns = [
    path('news_list/', cache_page(60*10), index, name='index'),
    path('new/<str:slug>', cache_page(300*10), detail, name='detail'),
    path('create/', cache_page(300*10), PostCreateView.as_view(), name='post_create'),
    re_path(r'^(?P<pk>\d+)/edit/$', cache_page(300*10), PostUpdateView.as_view(), name='post_edit'),
    re_path(r'^(?P<pk>\d+)/delete/$', cache_page(300*10), PostDeleteView.as_view(), name='post_delete'),
    path('categories/<int:pk>', cache_page(300*10), CategoryList.as_view(), name = 'category_list'),
    path('categories/<int:pk>/subscribe', subscribe, name='suscribe'),
]
