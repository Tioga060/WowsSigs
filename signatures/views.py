# Create your views here.
from django.http import HttpResponse
from models import *

def testview(request):
  newplayer = Player(playerid = '111',
    username = 'swagman',
    signature={"test":"test"})
  newplayer.save()

  return HttpResponse("<h1>Saved!</h1>")
