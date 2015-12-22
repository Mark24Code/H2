from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length = 50, blank = True)
    created_at = models.DateTimeField(auto_now_add = True)
    content = models.TextField(blank = True, null = True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
