from rest_framework import serializers

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    inputs = ToolInputSerializer(many=True)
    class Meta:
        model = Player
        fields = '__all__'
