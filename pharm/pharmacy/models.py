from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.phonenumber import PhoneNumber

from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.core.cache import cache 
from django.db.models import BooleanField, ExpressionWrapper, Q
from django.db.models.functions import Now


class CustomUser(AbstractUser):
    user_type_data = ((1, "AdminHOD"), (2, "Pharmacist"), (3, "Doctor"), (4, "PharmacyClerk"),(5, "Patients"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)

class Patients(models.Model):
    gender_category=(
        ('Male','Male'),
        ('Female','Female'),
    )
    admin = models.OneToOneField(CustomUser,null=True, on_delete = models.CASCADE)
    reg_no=models.CharField(max_length=30,null=True,blank=True,unique=True)
    gender=models.CharField(max_length=7,null=True,blank=True,choices=gender_category)
    first_name=models.CharField(max_length=20,null=True,blank=True)
    last_name=models.CharField(max_length=20,null=True,blank=True)
    dob=models.DateTimeField(auto_now_add= False, auto_now=False,null=True,blank=True)
    phone_number=models.CharField(max_length=10,null=True,blank=True)
    profile_pic=models.ImageField(default="patient.jpg",null=True,blank=True)
    age= models.IntegerField(default='0', blank=True, null=True)
    address=models.CharField(max_length=300,null=True,blank=True)
    date_admitted=models.DateTimeField(auto_now_add=True, auto_now=False)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return str(self.admin)



class AdminHOD(models.Model):
    gender_category=(
        ('Male','Male'),
        ('Female','Female'),
    )
    admin = models.OneToOneField(CustomUser,null=True, on_delete = models.CASCADE)
    emp_no= models.CharField(max_length=100,null=True,blank=True)
    gender=models.CharField(max_length=100,null=True,choices=gender_category)
    mobile=models.CharField(max_length=10,null=True,blank=True)
    address=models.CharField(max_length=300,null=True,blank=True)
    profile_pic=models.ImageField(default="admin.png",null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    date_employed=models.DateTimeField(auto_now_add=True, auto_now=False)
    objects = models.Manager()
    def __str__(self):
        return str(self.admin)
    


class Pharmacist(models.Model):
    gender_category=(
        ('Male','Male'),
        ('Female','Female'),
    )
    admin = models.OneToOneField(CustomUser,null=True, on_delete = models.CASCADE)
    emp_no=models.CharField(max_length=100,null=True,blank=True)
    age= models.IntegerField(default='0', blank=True, null=True)
    gender=models.CharField(max_length=100,null=True,choices=gender_category)
    mobile =models.CharField(max_length=10,null=True,blank=True)
    address=models.CharField(max_length=300,null=True,blank=True)
    profile_pic=models.ImageField(default="images2.png",null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    def __str__(self):
        return str(self.admin)

    
class Doctor(models.Model):
    gender_category=(
        ('Male','Male'),
        ('Female','Female'),
    )
    admin = models.OneToOneField(CustomUser,null=True, on_delete = models.CASCADE)
    emp_no=models.CharField(max_length=100,null=True,blank=True)
    age= models.IntegerField(default='0', blank=True, null=True)
    gender=models.CharField(max_length=100,null=True,choices=gender_category)
    mobile=models.CharField(max_length=10,null=True,blank=True)
    address=models.CharField(max_length=300,null=True,blank=True)
    profile_pic=models.ImageField(default="doctor.png",null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    def __str__(self):
        return str(self.admin)
	

class PharmacyClerk(models.Model):
    gender_category=(
        ('Male','Male'),
        ('Female','Female'),
    )
    admin = models.OneToOneField(CustomUser,null=True, on_delete = models.CASCADE)
    emp_no=models.CharField(max_length=100,null=True,blank=True)
    gender=models.CharField(max_length=100,null=True,choices=gender_category)
    mobile=models.CharField(max_length=10,null=True,blank=True)
    address=models.CharField(max_length=300,null=True,blank=True)
    profile_pic=models.ImageField(default="images2.png",null=True,blank=True)
    age= models.IntegerField(default='0', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    def __str__(self):
        return str(self.admin)
	
    

class Category(models.Model):
    name = models.CharField(max_length=50, blank=False, null=True)
    
    def __str__(self):
        return str(self.name)
	

    
class Prescription(models.Model):
    patient_id = models.ForeignKey(Patients,null=True, on_delete=models.SET_NULL)
    description=models.TextField(null=True)
    prescribe=models.CharField(max_length=100,null=True)
    date_precribed=models.DateTimeField(auto_now_add=True, auto_now=False)




class ExpiredManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().annotate(
            expired=ExpressionWrapper(Q(valid_to__lt=Now()), output_field=BooleanField())
        )

class Stock(models.Model):
    category = models.ForeignKey(Category,null=True,on_delete=models.CASCADE,blank=True)
    drug_imprint=models.CharField(max_length=6 ,blank=True, null=True)
    drug_name = models.CharField(max_length=50, blank=True, null=True)
    drug_color = models.CharField(max_length=50, blank=True, null=True)
    drug_shape = models.CharField(max_length=50, blank=True, null=True)
    quantity = models.IntegerField(default='0', blank=True, null=True)
    receive_quantity = models.IntegerField(default='0', blank=True, null=True)
    reorder_level = models.IntegerField(default='0', blank=True, null=True)
    manufacture= models.CharField(max_length=50, blank=True, null=True)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    drug_strength= models.CharField(max_length=10, blank=True, null=True)
    valid_from = models.DateTimeField(blank=True, null=True,default=timezone.now)
    valid_to = models.DateTimeField(blank=False, null=True)
    drug_description=models.TextField(blank=True,max_length=1000,null=True)
    drug_pic=models.ImageField(default="images2.png",null=True,blank=True)
    objects = ExpiredManager()
   
    def __str__(self):
        return str(self.drug_name)
   
    
class Dispense(models.Model):
    
    patient_id = models.ForeignKey(Patients, on_delete=models.DO_NOTHING,null=True)
    drug_id = models.ForeignKey(Stock, on_delete=models.SET_NULL,null=True,blank=False)
    dispense_quantity = models.PositiveIntegerField(default='1', blank=False, null=True)
    taken=models.CharField(max_length=300,null=True, blank=True)
    stock_ref_no=models.CharField(max_length=300,null=True, blank=True)
    instructions=models.TextField(max_length=300,null=True, blank=False)
    dispense_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)


class PatientFeedback(models.Model):
    id = models.AutoField(primary_key=True)
    patient_id = models.ForeignKey(Patients, on_delete=models.CASCADE)
    admin_id= models.ForeignKey( AdminHOD,null=True, on_delete=models.CASCADE)
    pharmacist_id=models.ForeignKey( Pharmacist,null=True, on_delete=models.CASCADE)
    feedback = models.TextField(null=True)
    feedback_reply = models.TextField(null=True)
    admin_created_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()





@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 1:
            AdminHOD.objects.create(admin=instance)
        if instance.user_type == 2:
            Pharmacist.objects.create(admin=instance,address="")
        if instance.user_type == 3:
            Doctor.objects.create(admin=instance,address="")
        if instance.user_type == 4:
            PharmacyClerk.objects.create(admin=instance,address="")
        if instance.user_type == 5:
            Patients.objects.create(admin=instance,address="")
       
       
       

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.adminhod.save()
    if instance.user_type == 2:
        instance.pharmacist.save()
    if instance.user_type == 3:
        instance.doctor.save()
    if instance.user_type == 4:
        instance.pharmacyclerk.save()
    if instance.user_type == 5:
        instance.patients.save()


   



 