from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.EmailField(max_length=122)
    phone = models.IntegerField(max_length=12)
    message = models.TextField()
    date = models.DateTimeField()
    
    
    def __str__(self):
        return self.name  # Show user name in admin panal