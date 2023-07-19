from django.db import models
from django.urls import reverse

BEATERS = (
    ('P', 'Porky'),
    ('C', 'Charcoal'),
    ('Z', 'Zephyr'),
    ('TJ', 'Therapist Joe'),
    ('KM', 'Krombopulos Michael'),
    ('PR', 'Period')
)

# Create your models here.
class Beat(models.Model):
    Demographic_Choices = [
        ('Teens', 'Teens'),
        ('Children', 'Children'),
        ('Adults', 'Adults'),
    ]

    Gender_Choices = [
        ('Boys', 'Boys'),
        ('Girls', 'Girls'),
        ('All', 'All'),
        ('Men', 'Men'),
        ('Women', 'Women'),
    ]

    Name = models.CharField(max_length=100)
    Demographic = models.CharField(max_length=100, choices=Demographic_Choices)
    Gender = models.CharField(max_length=100, choices=Gender_Choices)
    Description = models.TextField(max_length=250)

def __str__(self):
    return f'{self.name} ({self.id})'

def get_absolute_url(self):
    return reverse('detail', kwargs={'beat_id': self.id})

class Beating(models.Model):
    date = models.DateField()
    beater = models.CharField(
        max_length=2,
        choices=BEATERS,
    )
    beat = models.ForeignKey(Beat, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.get.beat_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']