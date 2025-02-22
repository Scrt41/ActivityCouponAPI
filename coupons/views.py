from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Coupon
from .serializers import CouponSerializer
from .services import get_filtered_coupons, deactivate_coupon

class CouponViewSet(viewsets.ModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer

    def get_queryset(self):
        status_filter = self.request.query_params.get('status')
        return get_filtered_coupons(status_filter)

    @action(detail=True, methods=['post'])
    def deactivate(self, request, pk=None):
        coupon = get_object_or_404(Coupon, pk=pk)
        deactivate_coupon(coupon)
        return Response({'message': 'Coupon deactivated'}, status=status.HTTP_200_OK)
