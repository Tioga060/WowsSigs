# Create your views here.
from django.http import HttpResponse
from django.conf import settings as djangoSettings
from serializers import *
from models import *
from forms import SignatureForm
from django.views.generic import TemplateView

def testview(request):
    p = Player(username="Jeff",playerid="123",signature={'test':False})
    p.save()
    return HttpResponse("<h1>Resized Gif</h1>")




class SignatureFormView(TemplateView):
    template_name = "signatures/new.html"

    def get_context_data(self, **kwargs):
        context = super(SignatureFormView, self).get_context_data(**kwargs)
        context.update(SignatureForm=SignatureForm())
        return context
