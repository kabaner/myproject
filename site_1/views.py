# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def header(request):
    html={}
    h_list=['HTTP_HOST','HTTP_USER_AGENT','OS','PATH_INFO','REMOTE_ADDR','REQUEST_METHOD','SERVER_PORT']
    for header_var in h_list:
        html[header_var]=request.META[header_var]
    print html
    return render(request, 'header.html',{ 'html':html })