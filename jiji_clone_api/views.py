from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, AllowAny
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action 
from django.contrib.auth.models import User
from .models import Product, Users
from .serializers import ProductSerializer, UserSerializer, BuyerSerializer, UsersSerializer


# for post permissions 
class PostPermission(BasePermission):
    message = 'Buyers' 
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return False

# Custom token class
class CustomizeToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomizeToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id})

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    # authentication_classes = (TokenAuthentication,)

    # action 
    @action(methods=['POST'], detail=True)
    def delete(self, *args, **kwargs):
        response = {'message': 'Not Allowed'}
        return Response(response, status = status.HTTP_400_BAD_REQUEST)



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (PostPermission,)
    authentication_classes = (TokenAuthentication,)


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    permission_classes = (PostPermission,)
    # authentication_classes = (TokenAuthentication,)

    # action 
    def create(self, request=None):
        if  ('first_name' in request.data) and ('last_name' in request.data) and ('location' in request.data) and('username' in request.data) and ('password' in request.data) and ('email' in request.data):
            first_name = request.data['first_name']
            last_name = request.data['last_name']
            location = request.data['location']
            username = request.data['username']
            password = request.data['password']
            email = request.data['email']


            try:
                user = User.objects.create_user(username = username, 
                                            first_name = first_name,
                                            last_name = last_name,
                                            email=email, 
                                            password=password
    )
                serializer_user = UserSerializer(user, many=False)
                users = Users.objects.create(user=user, location=location)
                serializer_users = UsersSerializer(users, many=False)
                response = {'message': 'user created', 'result': serializer_user.data, 'location': serializer_users.data}
                return Response(response, status = status.HTTP_200_OK)
            except:
                response = {'message': 'User exist'}
                return Response(response, status = status.HTTP_400_BAD_REQUEST)
        else:
            response = {'message': 'Required'}
            return Response(response, status = status.HTTP_400_BAD_REQUEST)
            
# custom permission for buyers, post only


class BuyerViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = BuyerSerializer
    permission_classes = (PostPermission,)
    authentication_classes = (TokenAuthentication)

    # action 
    def delete(self, *args, **kwargs):
        response = {'message': 'Not Allowed'}
        return Response(response, status = status.HTTP_400_BAD_REQUEST)

