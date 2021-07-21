from django.db import models
from django.urls import reverse


class Task(models.Model):
    PRIORITY = (
        ("High", "High"),
        ("Medium", "Medium"), 
        ("Low", "Low")
    )

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    due_date = models.DateField(null=True, blank=True)
    priority = models.CharField(max_length=50, choices=PRIORITY, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self): # new
        return reverse('update', kwargs={'pk': str(self.pk)})


    class Meta:
        ordering = ("complete",)