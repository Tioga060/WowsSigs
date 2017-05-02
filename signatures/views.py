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

def index(request):
    #p = Player(username="Jeff",playerid="123",signature={'test':False})
    #p.save()
    return render_to_response('signatures/index.html', RequestContext(request))




class SignatureFormView(TemplateView):
    template_name = "signatures/new.html"

    def get_context_data(self, **kwargs):
        context = super(SignatureFormView, self).get_context_data(**kwargs)
        context.update(SignatureForm=SignatureForm())
        return context
