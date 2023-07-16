from django.db import models

# Create your models here.

class Post(models.Model):
    author= models.CharField(max_length=100, null= False, blank= False, verbose_name='Автор')
    body = models.CharField(max_length=100, null=False, blank=False, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Дата и время создания')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='Дата и время изменения')

    def __str__(self):
        return f"{self.pk}. {self.author}"

