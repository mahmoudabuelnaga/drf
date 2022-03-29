from cgitb import lookup
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer
# Create your views here.

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)



class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_fields = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_fields = 'pk'

    def perform_delete(self, instance):
        super().perform_delete(instance)



@api_view(['GET','POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    if request.method == 'GET':
        # Detail
        if pk is not None:
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)

        # list
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)
        
    if request.method == 'POST':
        # create an item
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content')
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"invalid":"not good data"}, 400)



# api views paths
product_create_api_view = ProductListCreateAPIView.as_view()
product_detail_api_view = ProductDetailAPIView.as_view()
product_update_api_view = ProductUpdateAPIView.as_view()
product_delete_api_view = ProductDestroyAPIView.as_view()