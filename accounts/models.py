from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser
from .managers import CustomUserManager

# Create your models here.
class CustomUser(AbstractBaseUser):
    # username = NoneTrue) unique=True)
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    staff = models.BooleanField(default=False) #staff user or non super user
    superuser = models.BooleanField(default=False) #super user
    active = models.BooleanField(default=True) #can login
    timestamp = models.DateTimeField(default=timezone.now)


    USERNAME_FIELD = 'email' #username
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

 
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_superuser(self):
        "Is the user a admin member?"
        return self.superuser

    @property
    def is_active(self):
        return self.active




class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=15)
    #image = models.ImageField(upload_to = "seller/productimages", default = None, null = True, blank = True)
    #image = models.FilePathField(path="/pics")
    price = models.FloatField()
    brand = models.CharField(max_length=1000)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        """String for representing a model object"""
        return self.product_name
