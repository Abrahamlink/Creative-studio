from django import forms


class PlaceholderForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(PlaceholderForm, self).__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['placeholder'] = field.help_text


class EmailLetterForm(PlaceholderForm):
    user_name = forms.CharField(label='Имя', required=True, help_text='Выше имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    from_email = forms.EmailField(label='Email-адрес', required=True, help_text='@mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    # password = forms.CharField(label='Пароль', required=True, help_text='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(label='Тема-письма', required=True, help_text='Тема письма', widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label='Сообщение', help_text='Текст сообщения', widget=forms.Textarea(attrs={'class': 'form-control'}), required=True)
