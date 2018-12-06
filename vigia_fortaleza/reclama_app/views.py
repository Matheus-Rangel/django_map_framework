from django.urls import path
from map_app.views.flex import ReclamaView

#Imports do primeiro método
from django.core.mail import send_mail
from django.conf import settings
from django.http import *
from django.shortcuts import render
from django.views import View

class ReclamaFortalezaView(ReclamaView):
    def send_mail(request):
        send_mail('assunto teste', 'testando', settings.EMAIL_HOST_USER, ['milhousesmite@gmail.com'], fail_silently=False,)
        return HTTPResponse('Reclamação enviada com sucesso!')

    def redirect_email(request):
        return redirect('https://transparencia.fortaleza.ce.gov.br/index.php/faleConosco/')

