from django.conf import settings
from django.db import models
from django.utils import timezone


class AccessTable(models.Model):
    #worker = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length=100)
    card_number = models.CharField(max_length=50)
    sap_id = models.CharField(max_length=50)


    def publish(self):
        self.save()

    def __str__(self):
        return self.name + " " + self.sap_id
