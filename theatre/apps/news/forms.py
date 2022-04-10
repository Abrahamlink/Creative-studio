from .models import Comment
from django.forms import ModelForm, TextInput, Textarea


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text', 'author_email', 'site']
        widgets = {
            'author': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваше ИМЯ',
                'name': 'user_name',
                'type': "text"
            }),
            'text': Textarea(attrs={
                'placeholder': 'Введите текст комментария',
                'name': 'comment',
                'rows': 8,
                'class': 'form-control',
            }),
            'author_email': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваш EMAIL',
                'name': 'email',
                'type': "text"
            }),
            'site': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваш сайт (если конечно он есть)',
                'name': 'site',
                'type': "text"
            }),
        }
