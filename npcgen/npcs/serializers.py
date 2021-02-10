from rest_framework import serializers
from npcs.models import NPC

# NPC Serializer
class NPCSerializer(serializers.ModelSerializer):
  class Meta:
    model = NPC
    fields = '__all__'