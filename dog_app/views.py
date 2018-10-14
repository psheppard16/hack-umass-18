from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from dog_app.models import *
from django.http import JsonResponse
from dog_app.forms import *
from dog_app.serializers import *
from django.urls import reverse
from django.views import View


import logging
log = logging.getLogger('dog')

###########################################################################
#                             Dog VIEWS                                   #
#                                                                         #
###########################################################################


def HomeView(request):
    context = {'title': "Home",
               'user': request.user
               }
    return render(request, 'pages/home.html', context)


def BasicUploadView(request):
    if request.GET:
        photos_list = Photo.objects.all()
        return render(request, 'pages/home.html', {'photos': photos_list})
    else:
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save()
            data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)