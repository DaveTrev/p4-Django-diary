from django.db import models
from django.contrib.auth.models import User 
# Create your models here.


class diaryEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    learningOutcome = models.TextField(null=True, blank=True)
    activityType = models.TextField(null=True, blank=True)
    timeSpent = models.DecimalField(max_digits=4, decimal_places=2)
    cpdCredits = models.DecimalField(max_digits=4, decimal_places=2)
    practiceImpact = models.TextField(null=True, blank=True)


def __str__(self):
    return self.title

    class Meta:
        ordering = ['date']

