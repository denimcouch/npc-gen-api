from npcs.models import NPC
from rest_framework import viewsets, permissions
from .serializers import NPCSerializer

# NPC Viewset
class NPCViewSet(viewsets.ModelViewSet):
  queryset = NPC.objects.all()
  permission_classes = [
    permissions.AllowAny
  ]
  serializer_class = NPCSerializer
