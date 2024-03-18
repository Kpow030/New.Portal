from django.urls import path, re_path
from .views import index, detail, PostCreateView, PostUpdateView, PostDeleteView


urlpatterns = [

    path('news_list/', index, name='index'),
    path('new/<str:slug>', detail, name='detail'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    re_path(r'^(?P<pk>\d+)/edit/$', PostUpdateView.as_view(), name='post_edit'),
    re_path(r'^(?P<pk>\d+)/delete/$', PostDeleteView.as_view(), name='post_delete'),
]
