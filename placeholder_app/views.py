from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from placeholder_app.models import *
from placeholder_app.forms import *
from placeholder_app.serializers import *
from django.urls import reverse

import logging
log = logging.getLogger('placeholder')

###########################################################################
#                             Placeholder VIEWS                           #
#                                                                         #
###########################################################################


# def HomeView(request):
#     context = {'title': "Home",
#                'user': request.user
#                }
#     return render(request, 'pages/home.html', context)