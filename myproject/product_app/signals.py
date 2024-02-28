# myapp/signals.py
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from .models import Product

@receiver(pre_save, sender=Product)
def update_created_at(sender, instance, **kwargs):
    instance.created_at = timezone.now()
