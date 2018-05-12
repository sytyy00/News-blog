from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User


class Articles(models.Model):
    title = models.CharField(max_length=128,verbose_name='Заголовок поста')
    post = RichTextUploadingField(verbose_name='Пост')
    date = models.DateTimeField(verbose_name='Дата')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Автор')

    def __str__(self):
        return self.title

