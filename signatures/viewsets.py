from rest_framework import viewsets, response
from models import *
from serializers import *
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
    def list(self, request):
        queryset = Player.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return response.Response(serializer.data)

    def retrieve(self, request, pk='cookie'):
        queryset = Player.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = PlayerSerializer(user)
        return response.Response(serializer.data)
