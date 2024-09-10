from django.db import models
# Create your models here.
class userdetails(models.Model):
 username=models.CharField(max_length=50)
 usercontact=models.IntegerField()
 useremail=models.CharField(max_length=50)
 userpassword=models.CharField(max_length=20)
def __str__(self):
 return self.username
class CustomerEnquiry(models.Model):
 id = models.IntegerField(primary_key=True,max_length=10,default=None),
 cust_name=models.CharField(max_length=50)
 cust_email=models.CharField(max_length=50)
 cust_contact=models.CharField(max_length=12)
 date=models.DateField()
 cust_source=models.CharField(max_length=50)
 cust_destination=models.CharField(max_length=50)
 type_of_property=models.CharField(max_length=50)
 cust_note=models.CharField(max_length=200)
