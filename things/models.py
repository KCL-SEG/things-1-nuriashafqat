from django.db import models
from django.db.models import Model
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator


class Thing(models.Model):
    name = models.CharField(max_length=30,blank=False, unique = True)
    description = models.TextField(max_length=120, blank=True, unique = False)
    quantity = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )


