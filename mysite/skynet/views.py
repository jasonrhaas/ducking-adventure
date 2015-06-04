from skynet.models import Messages
from skynet.serializers import SkynetSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers

class SkynetList(generics.ListCreateAPIView):
    queryset = Messages.objects.all()
    serializer_class = SkynetSerializer

# @api_view(('GET',))
# def api_root(request, format=None):
#     return Response({
#         # 'users': reverse('user-list', request=request, format=format),
#         'messages': reverse('message-list', request=request, format=format)
#     })

# def get(self, request, format=None):
#     user_count = User.objects.count()

    def get(self, request, format=None):
        total_count = Messages.objects.count()
        content = {'total_count': total_count}

        city_count = Messages.objects.values_list('city', flat=True).count()
        username_count = Messages.objects.values_list('username', flat=True).count()
        content = {'cities': city_count, 'users': username_count}
        return Response(content)
