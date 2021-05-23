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
	impf=models.ImageField(upload_to='Profiles/',default="Note.jpg")
	gender=models.CharField(max_length=10,choices=g,default="F")
	organization_name=models.CharField(max_length=120,default="ngo")
	hospital_name=models.CharField(max_length=120,default="ap")
	phone_no=models.CharField(null=True,default="1234567890",max_length=10)
	pan_no=models.CharField(max_length=10,default="ABC1234DE5")
	address=models.CharField(max_length=200,default="Tirupathi")

class MedicineInfo(models.Model):
	pharmacy_name=models.CharField(max_length=500)
	medicine_name=models.CharField(max_length=120)
	quantity=models.CharField(max_length=30)
	batch_no=models.IntegerField(unique=True)
	category=models.CharField(max_length=120)
	production_date=models.DateField()
	entry_date=models.DateField()
	expiry_date=models.DateField()
	tablets_required=models.CharField(max_length=100)
	org_name=models.CharField(max_length=300)
	uid=models.ForeignKey(User,on_delete=models.CASCADE)

class DonationInfo(models.Model):
	username=models.CharField(max_length=120)
	org_name=models.CharField(max_length=120)
	total_tablets=models.IntegerField(null=True)
	donated_tablets=models.IntegerField()
	remaining_tablets=models.IntegerField()
	donated_date=models.DateField()
	pid=models.ForeignKey(MedicineInfo,on_delete=models.CASCADE)

class ServiceBox(models.Model):
	name=models.CharField(max_length=100)
	email=models.EmailField(max_length=50)
	change_role=models.CharField(max_length=1000)
	img= models.ImageField(upload_to='Profiles/',default="profile.png")

class Export(models.Model):
	is_medicinist = models.BooleanField(default=False)
	#age = models.IntegerField(default=10)
	u = models.OneToOneField(User,on_delete=models.CASCADE)

@receiver(post_save,sender=User)
def createpf(sender,instance,created,**kwargs):
	if created:
		Export.objects.create(u=instance)

