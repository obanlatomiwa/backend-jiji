from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action 
from .models import Product
from .serializers import ProductSerializer, UserSerializer

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)

    # action 
    @action(methods=['POST'], detail=True)
    def delete(self, *args, **kwargs):
        response = {'message': 'Not Allowed'}
        return Response(response, status = status.HTTP_400_BAD_REQUEST)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    # action 
    @action(methods=['POST'], detail=True)
    def delete(self, *args, **kwargs):
        response = {'message': 'Not Allowed'}
        return Response(response, status = status.HTTP_400_BAD_REQUEST)
