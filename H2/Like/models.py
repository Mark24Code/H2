from django.db import models

class Like(models.Model):
    user_id = models.CharField(default=0,max_length=100)#所属用户id
    blog_id = models.CharField(default=0,max_length=100)#所属博客id
    created_at = models.DateTimeField(auto_now_add=True)#创建时间

    def __str__(self):
        return "Like:= user_id:{},blog_id:{}".format(self.user_id,self.blog_id)

    class Meta:
        db_table = 'like'
        verbose_name = '点赞'
        ordering = ['id']
