from django.db import models
from tinymce import models as mce_models
from transliterate import translit

from django.utils import timezone


def upload_location(instance, filename):
    return "%s/%s" % ('video', translit(filename, 'ru', reversed=True))


class NewsPost(models.Model):
    title = models.CharField('Название поста', max_length=50)
    pubdate = models.DateTimeField('Дата и время события')
    register_date = models.DateField(auto_now=True)
    studio_name = models.CharField('Название студии (если это "новость")', max_length=150, blank=True, default='Текущая')
    text = mce_models.HTMLField('Текст статьи')
    small_description = mce_models.HTMLField('Небольшое описание мероприятия', blank=True)
    preview_image = models.ImageField('Основное изображение поста', upload_to='posts/')
    type = models.ManyToManyField('ActionType', blank=True, related_name='actions')

    def __str__(self):
        return self.title

    def display_type_name(self):
        return ', '.join([t['title'] for t in self.type.values()])

    def was_published_recently(self):
        return self.pubdate >= (timezone.now() - timezone.timedelta(days=7))

    class Meta:
        verbose_name = 'Новостной пост'
        verbose_name_plural = 'Новости'


class ImagePost(models.Model):
    product = models.ForeignKey(NewsPost, on_delete=models.CASCADE)
    tag = models.ManyToManyField('Tag', blank=True, related_name='images')
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
    video = models.CharField(blank=True, null=True, max_length=400)
    text_under = mce_models.HTMLField(blank=True)

    class Meta:
        verbose_name = 'Изображение или видео для поста'
        verbose_name_plural = 'Изображения или видео'


class Comment(models.Model):
    post = models.ForeignKey('NewsPost', on_delete=models.CASCADE)
    text = models.TextField('Текст комментария')
    pubdate = models.DateTimeField(auto_now=True)
    author = models.CharField('Имя пользователя', max_length=50)
    author_email = models.EmailField('Mail пользователя', max_length=120)
    site = models.URLField('Сайт', blank=True, null=True)

    class Meta:
        verbose_name = 'Комментарий к посту'
        verbose_name_plural = 'Комментарии'


class Tag(models.Model):
    title = models.CharField('Название тега', max_length=255)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги для изображений'

    def __str__(self):
        return self.title


class ActionType(models.Model):
    title = models.CharField('Название типа', max_length=255)

    class Meta:
        verbose_name = 'Тип действия'
        verbose_name_plural = 'Типы действий'

    def __str__(self):
        return self.title
