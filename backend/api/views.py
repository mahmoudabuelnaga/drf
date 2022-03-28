import re
from django.shortcuts import render
from django.http import JsonResponse
from products.models import Product
from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.serializers import ProductSerializer

# Create your views here.

@api_view(["GET"])
def api_home(request, *args, **kwargs):
    """
        DRF API view
    """
    instance = Product.objects.all().order_by("?").first()
    data1 = {}
    if instance:
        # data = model_to_dict(instance, fields=["id","title",'content','price','sale_price'])
        data2 = ProductSerializer(instance).data
    return Response(data2)