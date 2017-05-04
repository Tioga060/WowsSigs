# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings as djangoSettings
from serializers import *
from models import *
from forms import SignatureForm
from django.views.generic import TemplateView
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django_openid_auth import views as oauth_views

def index(request):
    #p = Player(username="Jeff",playerid="123",signature={'test':False})
    #p.save()
    return render_to_response('signatures/index.html', RequestContext(request))

def register_user(request):
    return oauth_views.login_complete(request,register_user_callback)
    
def register_user_callback(user_info):
    dashpos = user_info.index("-")
    playerid = user_info[dashpos-10:dashpos]
    username = user_info[dashpos+1:-1]
    p = Player(username=username,playerid=playerid,signature={'test':False})
    p.save()

class SignatureFormView(TemplateView):
    template_name = "signatures/new.html"

    def get_context_data(self, **kwargs):
        context = super(SignatureFormView, self).get_context_data(**kwargs)
        context.update(SignatureForm=SignatureForm())
        return context
