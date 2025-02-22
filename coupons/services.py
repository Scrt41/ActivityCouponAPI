from django.utils.timezone import now
from .models import Coupon

def get_filtered_coupons(status):
    if status == 'active':
        return Coupon.objects.filter(is_active=True, expiry_date__gte=now().date())
    elif status == 'expired':
        return Coupon.objects.filter(expiry_date__lt=now().date())
    return Coupon.objects.all()

def deactivate_coupon(coupon):
    coupon.is_active = False
    coupon.save()
    return coupon
