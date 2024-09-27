from django.db import models
from model_utils.models import TimeStampedModel, SoftDeletableModel

# Create your models here.
class Transfer(TimeStampedModel, SoftDeletableModel):
    hbl = models.TextField(max_length=50, null=False, blank=True)
    name = models.TextField(max_length=100, null=False, blank=True)
    city = models.TextField(max_length=50, null=False, blank=True)
    state = models.TextField(max_length=25, null=False, blank=True)
    warehouse = models.TextField(max_length=5, null=False, blank=True)

    def __str__(self):
        return self.hbl