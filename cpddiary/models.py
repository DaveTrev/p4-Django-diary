from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError


def validate_positive_decimal(value):
    if value < 0.5:
        raise ValidationError("Value must be greater than or equal to 0.5")

# change validators to min value 0.5 explain on form 
# what that means and link to about page


class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
                             blank=True)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200, blank=False)
    learningOutcome = models.TextField(null=True, blank=False)
    activityType = models.TextField(null=True, blank=False)
    timeSpent = models.DecimalField(max_digits=4, decimal_places=2,
                                    validators=[validate_positive_decimal])
    cpdCredits = models.DecimalField(max_digits=4, decimal_places=2,
                                     validators=[validate_positive_decimal])
    practiceImpact = models.TextField(null=True, blank=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['date']
        verbose_name_plural = "Entries"

