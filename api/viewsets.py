from rest_framework import viewsets
from api import serializers
from usuarios import models

class UsuariosViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UsuariosSerializer
    queryset = models.Usuario.objects.all()