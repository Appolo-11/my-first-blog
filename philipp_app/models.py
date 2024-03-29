from django.conf import settings
from django.db import models
from django.utils import timezone


class AccessTable(models.Model):
    #worker = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ST = 'ST'
    OH = 'OH'
    WT = 'WT'
    LAPTOP_STATUS_CHOICES = [
    ('OH', 'On hands'),
    ('ST', 'In storage'),
    ('WT', 'Waiting'),
]
    name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length=100)
    card_number = models.IntegerField(unique=True) #models.CharField(max_length=50)
    sap_id = models.CharField(max_length=50, unique=True)
    laptop_access = models.BooleanField()
    terminal_access = models.BooleanField()
    # laptop_number = models.IntegerField()
    # laptop_status = models.CharField(max_length=50, choices=LAPTOP_STATUS_CHOICES, default=ST,)
    if laptop_access:
    	laptop_number = models.IntegerField(unique=True)
    	laptop_status = models.CharField(max_length=50, choices=LAPTOP_STATUS_CHOICES, default=ST,unique=True)
    def publish(self):
        self.save()

    def __str__(self):
        return self.name + " " + self.last_name + " "+ str(self.card_number) + " " + self.sap_id
