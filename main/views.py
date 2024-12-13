from django.http import HttpResponseNotFound
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import Product, Review
from main.serializers import ReviewSerializer, ProductListSerializer, ProductDetailsSerializer


@api_view(['GET'])
def products_list_view(request):
    products = Product.objects.all()
    serializer = ProductListSerializer(products, many=True)
    return Response(serializer.data)


class ProductDetailsView(APIView):
    def get(self, request, product_id):
        productdetails = Product.objects.filter(id=product_id)
        if not productdetails:
            return HttpResponseNotFound("<h1>404</h1><p>No such product exists.</p>")
        else:
            serializer = ProductDetailsSerializer(productdetails, many=True)
            return Response(serializer.data)


# доп задание:
class ProductFilteredReviews(APIView):
    def get(self, request, product_id):
        query = request.GET.get("mark")
        if query is not None:
            productrev = Review.objects.filter(product_id=product_id, mark=query)
        else:
            productrev = Review.objects.filter(product_id=product_id)
        serializer = ReviewSerializer(productrev, many=True)
        return Response(serializer.data)
