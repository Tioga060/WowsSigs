# Create your views here.
from django.http import HttpResponse
from django.conf import settings as djangoSettings
import signatures
from models import *

def testview(request):
    inpath = djangoSettings.MEDIA_ROOT+"backgrounds/test2.gif"
    outpath = djangoSettings.STATIC_ROOT+"signatures/testout2.gif"
    signatures.createSignatureGif(inpath, outpath, {})
    return HttpResponse("<h1>Resized Gif</h1>")
