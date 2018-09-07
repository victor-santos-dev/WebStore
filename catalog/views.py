from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from catalog.models import Product,Variation,ImageProduct
from catalog.serializers import VariationSerializer

@csrf_exempt
def variation_list(request):
    """
    List all code Variations, or create a new Variation.
    """
    if request.method == 'GET':
        variations = Variation.objects.all()
        serializer = VariationSerializer(variations, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = VariationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def variation_detail(request, pk):
    """
    Retrieve, update or delete a code Variation.
    """
    try:
        variation = Variation.objects.get(pk=pk)
    except variation.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = VariationSerializer(variation)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = VariationSerializer(Variation, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        variation.delete()
        return HttpResponse(status=204)