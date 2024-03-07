from django.db import models
from auth_app.models import User


class HealthReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hb = models.IntegerField()
    bp = models.CharField(max_length=10)
    sleep_time = models.DateTimeField()
    dpf = models.FloatField()

    def __str__(self):
        return f"{self.user.first_name} - Report"


class Audit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.FloatField()

    def __str__(self):
        return f"{self.user.first_name} - Audit"
