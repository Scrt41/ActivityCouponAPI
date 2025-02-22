from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CouponViewSet

router = DefaultRouter()
router.register(r'coupons', CouponViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
