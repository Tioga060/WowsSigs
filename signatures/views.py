# Create your views here.
from django.http import HttpResponse
from django.conf import settings as djangoSettings
from serializers import *
from rest_framework_mongoengine import viewsets
from models import *

def testview(request):
    p = Player(username="Jeff",playerid="123",signature={'test':False})
    p.save()
    return HttpResponse("<h1>Resized Gif</h1>")


class PlayerViewSet(viewsets.ModelViewSet):
    '''
    Contains information about a command-line Unix program.
    '''
    lookup_field = 'playerid'
    serializer_class = PlayerSerializer

    def get_queryset(self):
        return Player.objects.all()
