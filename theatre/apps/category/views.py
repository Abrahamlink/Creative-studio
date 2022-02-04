from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from .models import Teacher, Studio
from .forms import EmailLetterForm
from email.mime.text import MIMEText
from .email_data import data
import smtplib


def index(request):
    template = 'category/main.html'
    return render(request, template, None)


def contacts(request):
    template = 'category/contacts.html'
    teachers = Teacher.objects.all()
    studio = Studio.objects.get(pk=1)
    return render(request, template, {'teachers': teachers, 'studio': studio})


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
                server.sendmail(from_email, data['default'], msg.as_string())
                server.quit()
            except Exception as ex:
                print(ex)
                return HttpResponse('<h1 style="text-align: center;">Ошибка в теле письма.</h1>'
                                    '<h4 style="text-align: center;">Для отправки нужен <span style="color: '
                                    'blue;">Gmail</span></h4> '
                                    '<p style="text-align: center;">...или вы просто ввели неверный пароль</p>')
            return redirect('contacts')
    else:
        return HttpResponse('Неверный запрос')
    return render(request, template, {'form': form})


def render_colors_and_fonts_from_site(request):
    template = 'category/color_scheme.html'
    colors_list = ['#1f1f1f', '#1b1b1b', '#282828', '#353535', '#cbcbcb',
                   '#cbcbcb80', '#333333', '#4949ac', 'green', '#57575780',
                   '#dcdcdc', '#7a7a7a', '#818181', '#6d6d6d4d', '#f1f1f1',
                   '#33333380', '#ba2b18', '#bd2130', '#c82333', '#9b1454',
                   '#ba6818', '#E35764', '#CF4FA3', '#E79358', '#f5daeb',
                   '#f8e1d0', '#f1cae3', '#daf5e4', '#3d3d3d'
                   ]
    colors_list = [color[1:] if color[0] == '#' else color for color in colors_list]
    fonts_list = ['Roboto', 'Arial', 'Helvetica', 'sans-serif', 'Oswald',
                  'Montserrat', 'Tenor Sans']
    context = {
        'colors': colors_list,
        'fonts': sorted(fonts_list)
    }
    return render(request, template, context)


class MyAjaxView(View):
    def get(self, request):
        text = request.GET.get('button_text')
        if _is_ajax(request):
            return JsonResponse({'text': text}, status=200)
        return render(request, 'category/test.html', None)


def _is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
