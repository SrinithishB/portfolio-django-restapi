from django.db import models

# Create your models here.
from django.db import models

class Projects(models.Model):
    pname=models.CharField(max_length=200)
    pdescription=models.CharField(max_length=500)
    link=models.CharField(max_length=500)
    
    def __str__(self) -> str:
        return f'{self.pname}, {self.pdescription}, {self.link}'
    