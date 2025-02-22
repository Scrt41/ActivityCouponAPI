from django.db import models
from django.utils.timezone import now

class Coupon(models.Model):
    id = models.AutoField(primary_key=True)  # Primary key
    code = models.CharField(max_length=50, unique=True)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    is_active = models.BooleanField(default=True)
    expiry_date = models.DateField()
    usage_count = models.PositiveIntegerField(default=0, editable=False)  # Read-only
    min_order_value = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    max_discount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp

    def is_expired(self):
        return self.expiry_date < now().date()

    def __str__(self):
        return self.code
