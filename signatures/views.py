# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings as djangoSettings
from serializers import *
from models import *
import random
from forms import SignatureForm
from django.views.generic import TemplateView
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django_openid_auth import views as oauth_views
import uuid

def index(request):
    #p = Player(username="Jeff",playerid="123",signature={'test':False})
    #p.save()
    response = render_to_response('signatures/index.html', RequestContext(request))
    cookie = str(uuid.uuid1()) + str(random.randint(1, 9999999999))
    if('tmoe_wows_session' not in request.COOKIES):
        response.set_cookie('tmoe_wows_session',cookie)
    return response

def register_user(request):
    result = oauth_views.login_complete(request,register_user_callback)
    if(str(result)!="true"):
        return result
    return redirect("/signatures/")

def register_user_callback(request, user_info):


    dashpos = user_info.index("-")
    playerid = user_info[dashpos-10:dashpos]
    username = user_info[dashpos+1:-1]
    p, created = Player.objects.get_or_create(playerid = playerid)
    p.username = username

    if(created):
        p.signature={'test':False}
    p.cookie = request.COOKIES['tmoe_wows_session']
    p.save()

class SignatureFormView(TemplateView):
    template_name = "signatures/new.html"

    def get_context_data(self, **kwargs):
        context = super(SignatureFormView, self).get_context_data(**kwargs)
        context.update(SignatureForm=SignatureForm())
        return context
