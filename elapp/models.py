from django.db import models

# Create your models here.
PRIORITY=(('danger','頻出'),('info','重要'),('success','基本'))
class elModel(models.Model):
    word=models.CharField(max_length=25)
    #mean=models.CharField(max_length=100)
    priority= models.CharField(
        max_length=50,
        choices = PRIORITY
    )

class Newword(models.Model):
    word = models.CharField(max_length=25)
    # date = models.DateField()
    mean = models.CharField(max_length=100, null=True)
    useful = models.PositiveIntegerField("the number of access", default=1)
    
    priority= models.CharField(
    max_length=50,
    choices = PRIORITY,
    null = True
    )
    def  __str__(self):
        return '{}/{}'.format(self.word, self.mean)