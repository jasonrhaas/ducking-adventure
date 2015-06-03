from skynet.models import Messages
from skynet.serializers import SkynetSerializer
from rest_framework import generics


class SkynetList(generics.ListCreateAPIView):
    queryset = Messages.objects.all()
    serializer_class = SkynetSerializer