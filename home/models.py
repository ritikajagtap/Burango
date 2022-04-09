from django.db import models

# Create your models here.
# makemigrations - creATE changes and store in a file
#migrate - apply the pending changes created by makemigrations
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=122)
    address = models.CharField(max_length=122)
    description = models.TextField()
    date = models.DateField()
    def __str__(self):
        return str(self.name)