""" RevenueStream views"""

from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from src.api.serializers.revenue_stream import RevenueStreamSerializer
from src.api.models import (
    RevenueStream,
    Product
)


class RevenueStreamListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer)
    serializer_class = RevenueStreamSerializer
    queryset = RevenueStream.objects.all()

    def list(self, request, *args, **kwargs):
        try:
            product = Product.objects.get(pk=kwargs['product_id'])
        except Product.DoesNotExist:
            message = 'Product does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        queryset = product.revenue_streams.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        try:
            product = Product.objects.get(pk=kwargs['product_id'])
        except Product.DoesNotExist:
            message = 'Product does not exist'
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        data = request.data
        exists = RevenueStream.objects.all().filter(
            name__icontains=data['name'],
            product__name__iexact=product.name
        )
        if len(exists) > 0:
            message = 'That revenue stream already exists'
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        serializer_context = {
            'request': request,
            'product': product
        }
        serializer = self.serializer_class(
            data=data, context=serializer_context)
        serializer.is_valid(raise_exception=True)
        serializer.save(product=product)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
