from rest_framework import viewsets, response
from models import *
from serializers import *
import django.shortcuts
class PlayerViewSet(viewsets.ModelViewSet):
    '''
    Contains information about a command-line Unix program.
    '''
    queryset = Player.objects.all()
    lookup_field = 'playerid'
    serializer_class = PlayerSerializer

    #def destroy(self, request, *args, **kwargs):
    #    instance = self.get_object()
    #    self.get_serializer().destroy(instance)
    #    print("Instance destroyed!")
    #    return response.Response(status=status.HTTP_204_NO_CONTENT)
class PlayerCookieViewSet(viewsets.ModelViewSet):
    '''
    Contains information about a command-line Unix program.
    '''
    serializer_class = PlayerSerializer
    lookup_field = 'cookie'
    def list(self, request):
        queryset = Player.objects.all()
        serializer = PlayerSerializer(queryset, many=True)
        return response.Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Player.objects.all()
        user = django.shortcuts.get_object_or_404(queryset, cookie="")
        serializer = PlayerSerializer(user)
        return response.Response(serializer.data)
