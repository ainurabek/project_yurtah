from django.urls import path, include
from rest_framework import routers
from django.conf.urls import url
from blog import views
from blog.views import UserView, BlogViewSet, PostView, NewsView

app_name = 'api'

router = routers.DefaultRouter()
router.register('user', UserView, basename='user')
router.register('blog', BlogViewSet, basename='blog')
router.register('post', PostView, basename='post')
router.register('news', NewsView, basename='news')


urlpatterns = [

    url(r'^subscribe_blog/(?P<blog_id>\d+)/', views.subscribe_other_blog, name='subscribe_blog'),
    url(r'^subscribed_blog_list/(?P<user_id>\d+)/', views.list_subscribed_blogs, name='list_subscribed_blogs'),
    url(r'^newsfeed/', views.get_own_posts, name='get_own_posts'),
    url(r'^news/', views.get_other_posts, name='get_other_posts'),
    path('', include(router.urls))

]