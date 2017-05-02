# Create your views here.
from django.http import HttpResponse
from django.conf import settings as djangoSettings
import signatures
from models import *

def testview(request):
    print "test"
    return HttpResponse("<h1>Resized Gif</h1>")
