from django.db import models
from tinymce import models as mce_models
from phonenumber_field.modelfields import PhoneNumberField


class Teacher(models.Model):
    name = models.CharField('Имя', max_length=100)
    last_name = models.CharField('Фамилия', max_length=100)
    photo = models.ImageField(blank=True, upload_to='avatars/')
    status = models.CharField('Должность или специальность', max_length=250)
    description = mce_models.HTMLField('Описание перподавателя')
    phone_number = PhoneNumberField('Номер телефона', unique=True)
    email = models.EmailField('Mail преподавателя', blank=True, null=True, max_length=255)
    father_name = models.CharField('Отчество', blank=True, max_length=70)

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Список преподавателей'

    def __str__(self):
        return f'{self.name} {self.father_name}'
