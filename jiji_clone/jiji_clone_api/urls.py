from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import ProductViewSet, UserViewSet, BuyerViewSet 

router = routers.DefaultRouter()
router.register('products', ProductViewSet)
router.register('users', UserViewSet)
router.register('buyers', BuyerViewSet)






urlpatterns = [
    path('', include(router.urls))
]