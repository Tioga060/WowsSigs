from rest_framework_mongoengine import viewsets, response
from models import *
from serializers import *
class PlayerViewSet(viewsets.ModelViewSet):
    '''
    Contains information about a command-line Unix program.
    '''
    queryset = Player.objects.all()
    lookup_field = 'playerid'
    serializer_class = PlayerSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.get_serializer().destroy(instance)
        print("Instance destroyed!")
        return response.Response(status=status.HTTP_204_NO_CONTENT)
