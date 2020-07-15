from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action 
from django.contrib.auth.models import User
from .models import Product, Users
from .serializers import ProductSerializer, UserSerializer, BuyerSerializer

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)

    # action 
    @action(methods=['POST'], detail=True)
    def delete(self, *args, **kwargs):
        response = {'message': 'Not Allowed'}
        return Response(response, status = status.HTTP_400_BAD_REQUEST)

class PostPermission(BasePermission):
    message = 'Buyers'
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return False

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (PostPermission,)
    authentication_classes = (IsAdminUser)

    # action 
    @action(methods=['POST'], detail=True)
    def delete(self, *args, **kwargs):
        response = {'message': 'Not Allowed'}
        return Response(response, status = status.HTTP_400_BAD_REQUEST)


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    permission_classes = (PostPermission,)
    authentication_classes = (IsAdminUser)

    # action 
    @action(methods=['POST'], detail=True)
    def create(self, *args, **kwargs):
        response = {'message': 'Not Allowed'}
        return Response(response, status = status.HTTP_400_BAD_REQUEST)
# custom permission for buyers, post only


class BuyerViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = BuyerSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (PostPermission)

    # action 
    def delete(self, *args, **kwargs):
        response = {'message': 'Not Allowed'}
        return Response(response, status = status.HTTP_400_BAD_REQUEST)

