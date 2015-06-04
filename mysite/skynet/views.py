from skynet.models import Messages
from skynet.serializers import SkynetSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
import sys

class SkynetList(generics.ListCreateAPIView):
    queryset = Messages.objects.all()
    serializer_class = SkynetSerializer

    def get(self, request, format=None):

        e1 = None
        e2 = None
        try:
            city_count = Messages.objects.values_list('city', flat=True).count()
        except:
            e1 = sys.exc_info()[0]
        try:
            username_count = Messages.objects.values_list('username', flat=True).count()
        except:
            e2 = sys.exc_info()[0]

        if e1 or e2:
            errormsg = 'errors: {}, {}'.format(e1, e2)
            content = {'result': 'error', 'error': errormsg}
        else:
            content = {'result': 'success', 'cities': city_count, 'users': username_count}

        return Response(content)
