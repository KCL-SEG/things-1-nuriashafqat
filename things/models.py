from django.db import models

class Thing(models.Model):
    name = models.CharField(max_length=30,blank=False, unique = True)
    description = models.TextField(max_length=120, blank=True, unique = False)
    quantity = models.IntegerField(
        validators=[MaxValueValidator(100)]
    )


