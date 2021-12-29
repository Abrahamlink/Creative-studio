from django.shortcuts import render, redirect
# from django.template import loader
from django.http import HttpResponse
from .models import Teacher
from django.core.mail import send_mail, BadHeaderError
from .forms import EmailLetterForm
from django.conf import settings
from email.mime.text import MIMEText
from .email_data import data
import smtplib


def index(request):
    template = 'category/main.html'
    return render(request, template, None)


def contacts(request):
    template = 'category/contacts.html'
    teachers = Teacher.objects.all()
    return render(request, template, {'teachers': teachers})


def send_mail_latter(request):
    template = 'category/letter.html'
    if request.method == 'GET':
        form = EmailLetterForm()
    elif request.method == 'POST':
        # Server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        # если метод POST, проверим форму и отправим письмо
        form = EmailLetterForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            msg = MIMEText(message)
            msg['From'] = from_email
            msg['To'] = data['default']
            msg['Subject'] = subject + f' от {from_email}'
            try:
                server.login(from_email, form.cleaned_data['password'])
                server.sendmail(msg['From'], msg['To'], msg.as_string())
                server.quit()
            except Exception as ex:
                print(ex)
                return HttpResponse('<h1 style="text-align: center;">Ошибка в теле письма.</h1>'
                                    '<h4 style="text-align: center;">Для отправки нужен <span style="color: blue;">Gmail</span></h4>'
                                    '<p style="text-align: center;">...или вы просто ввели неверный пароль</p>')
            return redirect('contacts')
    else:
        return HttpResponse('Неверный запрос.')
    return render(request, template, {'form': form})


def render_colors_and_fonts_from_site(request):
    template = 'category/color_scheme.html'
    colors_list = ['#ba2b18', '#1b1b1b', '#282828', '#353535', '#cbcbcb',
                   '#cbcbcb80', '#333333', '#4949ac', 'green', '#57575780',
                   '#dcdcdc', '#7a7a7a', '#818181', '#6d6d6d4d'
                   ]
    fonts_list = ['Roboto', 'Arial', 'Helvetica', 'sans-serif', 'Oswald',
                  'Montserrat', 'Tenor Sans']
    context = {
        'colors': sorted(colors_list),
        'fonts': sorted(fonts_list)
    }
    return render(request, template, context)
