from django.db import models
from django.conf import settings
import pytz
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255, null=True)
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image =  models.ImageField(null=True, blank=False)
    file = models.FileField(upload_to='music', null=True, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    views = models.IntegerField(default=0)

    def _str_(self):
        return self.title
    
    def time_since(self):
        time_difference = timezone.now() - self.date
        # chuyển đổi khoảng thời gian thành đơn vị ngày, giờ và phút
        days = time_difference.days
        hours, remainder = divmod(time_difference.seconds, 3600)
        minutes, _ = divmod(remainder, 60)

        if days > 0:
            return f"{days} days ago"
        if hours > 0:
            return f"{hours} times ago"
        if minutes > 0:
            return f"{minutes} min ago"
        else:
            return "Now"
    
class Comment(models.Model):
    # delete blog -> delete comment
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateField(default=timezone.now)

