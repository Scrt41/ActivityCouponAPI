from rest_framework import serializers
from .models import Coupon
from django.utils.timezone import now

class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'
        read_only_fields = ['usage_count', 'created_at', 'updated_at']

    def validate_expiry_date(self, value):
        if value < now().date():
            raise serializers.ValidationError("Expiry date cannot be in the past.")
        return value
