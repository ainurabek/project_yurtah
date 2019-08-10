from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from blog.models import Blog, Post, Subscription


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','username', 'email')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'user','title', 'text', 'blog')


class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ('id', 'birth_date', 'location')
        depth = 2

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ('blog',)
        depth =2
