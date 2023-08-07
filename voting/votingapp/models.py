from django.db import models
# Create your models here.
from django.contrib.auth.models import User
import math
class Voteuser(models.Model):
    user=models.ManyToManyField(User,related_name='uservote')
    ochosen=models.CharField(max_length=40,null=True,blank=True)
    qid=models.IntegerField(null=True,blank=True)

    
    

class Vote(models.Model):
    vtitle=models.CharField(max_length=255)
    option1=models.CharField(max_length=40)
    option2=models.CharField(max_length=40)
    option3=models.CharField(max_length=40)
    option4=models.CharField(max_length=40)
    option1val=models.IntegerField(default=0)
    option2val=models.IntegerField(default=0)
    option3val=models.IntegerField(default=0)
    option4val=models.IntegerField(default=0)
    vote=models.IntegerField()
    user=models.ManyToManyField(User)

    def __str__(self):
        return self.vtitle


    def firstoption(self):
        if (self.vote and self.option1val) ==0:
            return self.option1val
        else:
            return (self.option1val/4)*100
            
    
    def secondoption(self):
        if (self.vote and self.option2val) ==0:
            return self.option2val
        else:
            return (self.option2val/4)*100
    
    def thirdoption(self):
        if (self.vote and self.option3val) ==0:
            return self.option3val
        else:
            return (self.option3val/4)*100
        
    def fourthoption(self):
        if (self.vote and self.option4val) ==0:
            return self.option4val
        else:
            return (self.option4val/4)*100
            

       