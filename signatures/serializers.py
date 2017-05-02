from rest_framework_mongoengine import serializers
from models import *
class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ('playerid', 'username', 'signature')
