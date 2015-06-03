# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# from skynet.models import Messages
# from skynet.serializers import SkynetSerializer
# from django.db.models import Count

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from skynet.models import Messages
from skynet.serializers import SkynetSerializer
from rest_framework.views import APIView


# @api_view(['GET'])
# def skynet_list(request, format=None):
#     """
#     List all snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         messages = Messages.objects.all()
#         serializer = SkynetSerializer(messages, many=True)
#         return Response(serializer.data)

class SkynetList(APIView):
    """
    List all messages, or create a new message.
    """
    def get(self, request, format=None):
        snippets = Messages.objects.all()
        serializer = SkynetSerializer(snippets, many=True)
        return Response(serializer.data)