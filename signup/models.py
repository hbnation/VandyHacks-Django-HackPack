from django.db import models

class Event(models.Model):
    description = models.CharField(max_length=255, blank=True)
    date = models.DateField('event date')
    def __str__(self):
        return self.description

class Role(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)
    selection = models.IntegerField(default=0)
    def __str__(self):
        return self.name
