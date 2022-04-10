from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main_page'),
    path('contacts', views.contacts, name='contacts'),
    path('contacts/send_letter', views.send_mail_latter, name='send_letter'),
    path('color_scheme', views.render_colors_and_fonts_from_site, name='scheme'),
]
