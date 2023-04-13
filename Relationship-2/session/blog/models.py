from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/', null=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    tag = models.ManyToManyField('TTag', blank=True)



    class Meta:
        db_table = 'blog'
    
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.content[:100]


class Comment(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'commnet'
    def __str__(self):
        return self.content + '  | ' + str(self.author)


class TTag(models.Model):
    name = models.CharField(max_length=20)
    class Meta:
        db_table = 'ttag'
    def __str__(self):
        return self.name


class Like(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'like'
    def __str__(self):
        return self.like
