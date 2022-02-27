from django.db import models

# Create your models here.

class FeedBack(models.Model):
    name=models.CharField(max_length=30,null=True, blank=True)
    email=models.EmailField(null=True, blank=True)
    phone=models.CharField(max_length=11,null=True, blank=True)
    desc=models.CharField(max_length=200,null=True, blank=True)
    date=models.DateField()

    def __str__(self):
        return(self.desc)


class CustomerAccount(models.Model):
    
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30,null=True, blank=True)
    account_active=models.BooleanField(default=True)
    phoneno=models.CharField(max_length=11,blank=True)
    image=models.ImageField(upload_to='', default="")
    totacreditpoints=models.IntegerField(default=0)
    
    

    def __str__(self):
        return(f"{self.id}--{self.name} ------------> Status :{self.totacreditpoints}".format(self.id,self.name,self.totacreditpoints))



class store_courses(models.Model):
    course_id=models.IntegerField()
    course_title=models.CharField(max_length=40)
    url=models.URLField()
    is_paid=models.BooleanField()
    price=models.IntegerField()
    num_subscribers=models.IntegerField()
    num_reviews=models.IntegerField()
    num_lectures=models.IntegerField()
    level=models.CharField(max_length=20)
    content_duration=models.FloatField()
    subject=models.CharField(max_length=30)
    class Meta:
        db_table='store_courses'