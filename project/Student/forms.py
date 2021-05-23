from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django import forms
from Student.models import MedicineInfo,User,ServiceBox,DonationInfo



class UsForm(UserCreationForm):
	password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"password"}))
	password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"confirm password"}))
	class Meta:
		model=User
		fields=['username','email']
		widgets={
		"username":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Username"}),
		"email":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter email"}),
		}

class ChpwdForm(PasswordChangeForm):
		old_password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"old password"}))
		new_password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"new password"}))
		new_password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"confirm password"}))
		class Meta:
			model=User
			fields=['oldpassword','newpassword','confirmpassword']
			
			
class UsPerm(forms.ModelForm):
	class Meta:
		model=User
		fields=["username","role"]
		widgets={
		"username":forms.TextInput(attrs={
			"class":"form-control",
			"readOnly":True,
			}),
		"role":forms.Select(attrs={
			"class":"form-control",
			}),
		}


class ImForm(forms.ModelForm):
	class Meta:
		model=User
		fields=["first_name","last_name","age","gender","impf","hospital_name","phone_no","pan_no","address",]
		widgets={
		"first_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter First name"}),
		"last_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Last name"}),
		"age":forms.NumberInput(attrs={"class":"form-control","placeholder":"Update your age"}),
 		"gender":forms.Select(attrs={"class":"form-control","placeholder":"select your gender"}),
		"hospital_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter organization name"}),
		"phone_no":forms.NumberInput(attrs={"class":"form-control","placeholder":"Enter phone number"}),
		"pan_no":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter pan number"}),
		"address":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter address"}),
		}
class GuestForm(forms.ModelForm):
	password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"password"}))
	password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"confirm password"}))
	class Meta:
		model=User
		fields=['username','email']
		widgets={
		"username":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Username"}),
		"email":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter email"}),
		}
		
class OrgForm(forms.ModelForm):
	class Meta:
		model=User
		fields=['username',"first_name","last_name",'email',"age","gender","organization_name","phone_no","pan_no","address"]
		widgets={
		"username":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Username"}),
		"email":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter email"}),
		"first_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter First name"}),
		"last_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Last name"}),
		"age":forms.NumberInput(attrs={"class":"form-control","placeholder":"Update your age"}),
 		"gender":forms.Select(attrs={"class":"form-control","placeholder":"select your gender"}),
		"organization_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter organization name"}),
		"phone_no":forms.NumberInput(attrs={"class":"form-control","placeholder":"Enter phone number"}),
		"pan_no":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter pan number"}),
		"address":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter address"}),
		}

class Medform(forms.ModelForm):
	class Meta:
		model=MedicineInfo
		fields=['pharmacy_name','medicine_name','quantity','batch_no','category','production_date','entry_date','expiry_date','impf']
		widgets={
		"pharmacy_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter pharmacy name"}),
		"medicine_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Medicine name"}),
		"quantity":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Quantity"}),
		"batch_no":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Batch number"}),
		"category":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter category"}),
		"production_date":forms.DateInput(attrs={"class":"form-control","placeholder":"YYYY-MM-DD"}),
		"entry_date":forms.DateInput(attrs={"class":"form-control","placeholder":"YYYY-MM-DD"}),
		"expiry_date":forms.DateInput(attrs={"class":"form-control","placeholder":"YYYY-MM-DD"}),

		}

class ServiceForm(forms.ModelForm):
	class Meta:
		model=ServiceBox
		fields=["name","email","change_role","impf"]
		widgets={
		"name":forms.TextInput(attrs={"class":"form-control","placeholder":"UserName",}),
		"email":forms.TextInput(attrs={"class":"form-control","placeholder":"email"}),
		"change_role":forms.TextInput(attrs={"class":"form-control","placeholder":"Request your role to change"})
		}

# class DonationForm(forms.ModelForm):
# 	class Meta:
# 		model=DonationInfo
# 		fields=['username','org_name','donated_tablets','donated_date']
# 		widgets={
# 		"username":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Username"}),
# 		"org_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Organization name"}),
# 		"total_tablets":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter total tablets"}),
# 		"donated_tablets":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Donated tablets"}),
# 		"remaining_tablets":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter remaining tablets"}),
# 		"donated_date":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Donated date"}),
# 		}


class RequestForm(forms.ModelForm):
	class Meta:
		model=DonationInfo
		fields=['pharmacy_name','medicine_name','required_tablets']
		widgets={
		"pharmacy_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter pharmacy name"}),
		"medicine_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Medicine name"}),
		"required_tablets":forms.TextInput(attrs={"class":"form-control","placeholder":"Tablets required"}),
		"category":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter category"}),
		"org_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter your organization name"}),
		}