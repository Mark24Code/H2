from django.db import models

class Comment(models.Model):
    blog_id = models.CharField(default=0,max_length=100)#所属博客id
    nickname = models.CharField(max_length=64, null=True)#评论者昵称
    mail = models.CharField(max_length=254)#评论者邮箱
    # like = models.BooleanField(default=False)#评论者点赞
    content = models.TextField(blank=True,null=True)#评论内容
    created_at = models.DateTimeField(auto_now_add=True)#创建时间

    def __str__(self):
        return "Comment:= name:{},content:{}".format(self.nickname,self.content[:10])

    class Meta:
        db_table = 'comment'
        verbose_name = '评论和点赞'
        ordering = ['blog_id']
