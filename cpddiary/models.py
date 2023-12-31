from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator

# ensures validation of only positive numbers
# issues in removing this function to solely use minvaluevalidator


def validate_positive_decimal(value):
    if value < 0.5:
        raise ValidationError("Cpd Credit must be greater than or = to 0.5")

# change validators to min value 0.5 explain on form
# database throwing error when removing function
# what that means and link to about page


class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
                             blank=True)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200, blank=False, verbose_name="Title")
    learningOutcome = models.TextField(null=True, blank=False,
                                       verbose_name="Learning Outcome")
    activityType = models.TextField(null=True, blank=False,
                                    verbose_name="Activity Type")
    timeSpent = models.CharField(max_length=20, verbose_name="Time Spent",
                                 null=True, blank=False,)
    cpdCredits = models.DecimalField(verbose_name="Cpd Credits Claimed",
                                     max_digits=4, decimal_places=2,
                                     validators=[MinValueValidator(0)])
    practiceImpact = models.TextField(null=True, blank=False,
                                      verbose_name="Practice Impact")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['date']
        verbose_name_plural = "Entries"
