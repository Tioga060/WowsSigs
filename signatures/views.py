# Create your views here.
from django.http import HttpResponse
from django.conf import settings as djangoSettings
from signatures import *
from models import *

def testview(request):
    inpath = djangoSettings.MEDIA_ROOT+"backgrounds/test.gif"
    outpath = djangoSettings.STATIC_ROOT+"signatures/testout.gif"
    signatures.createSignatureGif(inpath, outpath, {})
    return HttpResponse("<h1>Resized Gif</h1>")
