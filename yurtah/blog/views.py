from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from rest_framework import viewsets, generics
from django.contrib.auth.models import User
from django.db.models import Q
# Create your views here.

from blog.models import Blog, Post, Subscription
from blog.serializers import BlogSerializer, PostSerializer, UserSerializer, NewsSerializer


class UserView(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class BlogViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()

class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field='pk'


def subscribe_other_blog(request, blog_id):
    user = request.user
    blog = Blog.objects.get(id=blog_id)
    subscribed_blog = Subscription.objects.create(blog = blog, user=user, is_subscribe=True)
    subscribed_blog.save()
    return HttpResponse(blog)

def list_subscribed_blogs(request, user_id):
    user=User.objects.get(id=user_id)
    list_subscribed_blogs = Subscription.objects.filter(user=user, is_subscribe=True).values_list('blog_id')
    return HttpResponse(list_subscribed_blogs)

class NewsView(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = NewsSerializer


def get_own_posts(request):
    user = request.user
    blog = Blog.objects.filter(user=user)
    post = Post.objects.filter(blog__in=blog).all()
    return HttpResponse(post)

def get_other_posts(request):
    news = Post.objects.none().order_by('-created_date')
    for sub in Subscription.objects.filter(user=request.user):
        for post in sub.blog.post_blog.all():
            print(post)
            newsfeed = news | post
        return HttpResponse(newsfeed)




