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


@api_view(['GET', 'POST'])
def skynet_list(request):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        messages = Messages.objects.all()
        serializer = SkynetSerializer(messages, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SkynetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @csrf_exempt
# def skynet_list(request):
#     """
#     List all code skynets, or create a new skynet.
#     """
#     if request.method == 'GET':
#         skynets = Messages.objects.all()
#         serializer = SkynetSerializer(skynets, many=True)
#         return JSONResponse(serializer.data)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = SkynetSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data, status=201)
#         return JSONResponse(serializer.errors, status=400)

# @csrf_exempt
# def skynet_detail(request, pk):
#     """
#     Retrieve, update or delete a code skynet.
#     """
#     try:
#         skynet = Messages.objects.get(pk=pk)
#     except Messages.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = SkynetSerializer(skynet)
#         return JSONResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = SkynetSerializer(skynet, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data)
#         return JSONResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         skynet.delete()
#         return HttpResponse(status=204)