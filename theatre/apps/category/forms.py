from django import forms


class EmailLetterForm(forms.Form):
    user_name = forms.CharField(label='Name', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    from_email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(label='Тема', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label='Сообщение', widget=forms.Textarea(attrs={'class': 'form-control'}), required=True)
