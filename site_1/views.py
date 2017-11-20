# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def header(request):
    html=[]
    h_list=['HTTP_HOST','HTTP_USER_AGENT','OS','PATH_INFO','REMOTE_ADDR','REQUEST_METHOD','SERVER_PORT']
    for header_var in h_list:
        print '<tr width="150px"><th align="left" >%s</th><th align="left">%s</th></tr>' % (header_var,request.META[header_var])
        html.append('<tr width="150px"><th align="left" >%s</th><th align="left">%s</th></tr>' % (header_var,request.META[header_var]))
    return HttpResponse('<html><body><table border="1" width="300px" height="100px" ">%s</table></body></html>' % '\n'.join(html))