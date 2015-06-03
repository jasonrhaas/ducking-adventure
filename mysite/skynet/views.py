from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from skynet.models import Messages
from skynet.serializers import SkynetSerializer
from django.db.models import Count

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def skynet_list(request):
    """
    List all code skynets, or create a new skynet.
    """
    if request.method == 'GET':
        skynets = Messages.objects.all()
        serializer = SkynetSerializer(skynets, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SkynetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def skynet_detail(request, pk):
    """
    Retrieve, update or delete a code skynet.
    """
    try:
        skynet = Messages.objects.get(pk=pk)
    except Messages.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SkynetSerializer(skynet)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SkynetSerializer(skynet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        skynet.delete()
        return HttpResponse(status=204)