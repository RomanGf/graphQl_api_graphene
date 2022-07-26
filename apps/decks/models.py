from django.db import models
from apps.utils.models import Timestamps
# Create your models here.

class Deck(Timestamps):
    title = models.CharField(max_length=100)
    description = models.TextField()
    last_reviewed = models.DateTimeField(blank=True, null=True)

    def __str__(self) -> str:
        return self.title