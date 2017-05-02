# Create your views here.
from django.http import HttpResponse
from django.conf import settings as djangoSettings
from serializers import *
from models import *

def testview(request):
    p = Player(username="Jeff",playerid="123",signature={'test':False})
    p.save()
    return HttpResponse("<h1>Resized Gif</h1>")
