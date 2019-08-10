from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.



class Blog(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)



    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_blog(sender, instance, created, **kwargs):
    if created:
        Blog.objects.create(user=instance)
    instance.blog.save()

class Post(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='post_blog',  blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)


    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Follower(models.Model):
    follower = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('follower', 'following')

    def __unicode__(self):
        return u'%s follows %s' % (self.follower, self.following)


class Subscription(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE,  blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)

    is_subscribe = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'blog')
        verbose_name = 'Subscription'
        verbose_name_plural = 'Subscriptions'

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        pass

#