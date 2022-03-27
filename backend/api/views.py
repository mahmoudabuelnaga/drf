from django.shortcuts import render
from django.http import JsonResponse
from products.models import Product
from django.forms.models import model_to_dict

# Create your views here.

def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=["id","title",'content','price'])
        # data['id'] = model_data.id
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price
        # model instance (model_data)
        # turn a Python dictionary
        # return JSON to my client
    return JsonResponse(data)