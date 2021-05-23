from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

	
class User(AbstractUser):
	t = (
		(1,'Medicinist'),
		(2,'Org'),
		(3,'Anonymous'),
		)
	role = models.IntegerField(default=3,choices=t)
	g=[('M',"Male"),('F','Female')]
	age=models.IntegerField(default=10)
	impf=models.ImageField(upload_to='Medicines/',default="ngo1.jpg")
	gender=models.CharField(max_length=10,choices=g,default="F")
	organization_name=models.CharField(max_length=120,default="ngo")
	hospital_name=models.CharField(max_length=120,default="ap")
	phone_no=models.CharField(null=True,default="1234567890",max_length=10)
	pan_no=models.CharField(max_length=10,default="ABC1234DE5")
	address=models.CharField(max_length=200,default="Tirupathi")

class MedicineInfo(models.Model):
	#organization_name=models.CharField(max_length=120,default="ngo")
	pharmacy_name=models.CharField(max_length=500)
	medicine_name=models.CharField(max_length=120)
	quantity=models.CharField(max_length=30)
	batch_no=models.IntegerField(unique=True,null=True)
	category=models.CharField(max_length=120)
	production_date=models.DateField(null=True)
	entry_date=models.DateField(null=True)
	expiry_date=models.DateField(null=True)
	created_date=models.DateField(auto_now=True)
	# days_count=models.DateField(blank=True,null=True)
	# total_tablets=models.IntegerField(null=True)
	# donated_tablets=models.IntegerField(null=True)
	# remaining_tablets=models.IntegerField(null=True)
	# donated_date=models.DateField(auto_now=True)
	# required_tablets=models.IntegerField(null=True)
	uid=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
	impf=models.ImageField(upload_to='Medicines/',default="ngo1.jpg")

class DonationInfo(models.Model):
	username=models.CharField(max_length=120)
	medicine_name=models.CharField(max_length=120)
	pharmacy_name=models.CharField(max_length=500)
	org_name=models.CharField(max_length=120)
	total_tablets=models.IntegerField(blank=True,null=True)
	donated_tablets=models.IntegerField(blank=True,null=True)
	remaining_tablets=models.IntegerField(null=True)
	days_count=models.DateField(blank=True,null=True)
	created_date=models.DateField(auto_now=True)
	required_tablets=models.IntegerField(blank=True,null=True)
	donated_date=models.DateField(blank=True,null=True)
	pid=models.ForeignKey(MedicineInfo,on_delete=models.CASCADE,null=True)

class ServiceBox(models.Model):
	name=models.CharField(max_length=100)
	email=models.EmailField(max_length=50)
	change_role=models.CharField(max_length=1000)
	impf=models.ImageField(upload_to='Medicines/',default="ngo1.jpg")

class Export(models.Model):
	is_medicinist = models.BooleanField(default=False)
	#age = models.IntegerField(default=10)
	u = models.OneToOneField(User,on_delete=models.CASCADE)

@receiver(post_save,sender=User)
def createpf(sender,instance,created,**kwargs):
	if created:
		Export.objects.create(u=instance)
