from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import ProductViewSet, UsersViewSet, BuyerViewSet 

router = routers.DefaultRouter()
router.register('products', ProductViewSet)
router.register('users', UsersViewSet)
router.register('buyers', BuyerViewSet)






urlpatterns = [
    path('', include(router.urls))
]