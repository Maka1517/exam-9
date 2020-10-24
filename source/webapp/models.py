from django.contrib.auth import get_user_model
from django.db import models


class Photo(models.Model):
    picture = models.ImageField(upload_to='uploads', verbose_name='Картинка')
    text = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Подпись')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_DEFAULT, default=1,
                               related_name='articles', verbose_name='Автор')

    def __str__(self):
        return f'{self.text} {self.author}'

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'

