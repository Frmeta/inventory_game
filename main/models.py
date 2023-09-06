from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    
    # opsional
    date_added = models.DateField(auto_now_add=True)