from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Stats

@receiver(post_save, sender=User)
def create_stats(sender, instance, created, **kwargs):
    if created:
        Stats.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_stats(sender, instance, **kwargs):
    instance.stats.save()