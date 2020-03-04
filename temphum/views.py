from rest_framework import viewsets
from .models import TempHum
from .serializers import TempHumSerializer

class TempHumViewSet(viewsets.ModelViewSet):
    queryset = TempHum.objects.all().order_by('-created')
    serializer_class = TempHumSerializer