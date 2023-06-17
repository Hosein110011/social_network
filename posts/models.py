from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50)
    caption = models.TextField(max_length=512)
    is_active = models.BooleanField(default=True)
    is_public = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Post"


class PostFile(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    file = models.FileField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

# class Comment(models.Model):
#     pass



# class Like(models.Model):
#     pass