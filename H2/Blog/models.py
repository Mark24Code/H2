from django.db import models
from django.contrib.auth.models import Group, User

class Blog(models.Model):
    user_id = models.CharField(default=0,max_length=100)#所属用户id
    # belong_to = models.OneToOneField(User,null = True)#所属活动
    title = models.CharField(max_length=100)#标题
    content = models.TextField(blank = True, null = True)#内容
    tag = models.CharField(max_length = 50, default="无分组")#分类
    created_at = models.DateTimeField(auto_now_add = True)#创建时间
    is_use = models.BooleanField(default=True)#逻辑删除

    def __str__(self):
        return self.title

    class Meta:
        db_table = "blog"
        verbose_name = "博客"
        ordering = ['-created_at']
