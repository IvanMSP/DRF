from django.db import models

# Create your models here.


class Category(models.Model):
    description = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    class Meta:
       verbose_name_plural = "categories" 

    def __str__(self):
        return '{}'.format(self.description)
    
    