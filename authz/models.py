from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class CustomUserManager(BaseUserManager):
    def _create_user(self,email,password, first_name, last_name, phone_num, date_of_birth,sex, country,state_of_origin, address,**extra_fields):
        if not email:
            raise valueerror("Email must be provided")
        if not password:
            raise valueerror("Password must be provided")

        user = self.model(
            email  = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            phone_num = phone_num,
            date_of_birth = date_of_birth,
            sex = sex,
            country = country,
            state_of_origin = state_of_origin,
            address= address,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, first_name, last_name,phone_num, date_of_birth,sex,country,state_of_origin,address, **extra_fields):
        extra_fields.setdefault('is_staff',False)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',False)
        extra_fields.setdefault('is_email_verified',False)
        extra_fields.setdefault('is_document_submitted',False)
        extra_fields.setdefault('is_document_verified',False)
        return self._create_user(email, password,first_name, last_name, phone_num, date_of_birth,sex, country, state_of_origin, address)

    def create_superuser(self, email, password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_email_verified',True)
        extra_fields.setdefault('is_document_submitted',True)
        extra_fields.setdefault('is_document_verified',True)
        return self._create_user(email, password,first_name=None, last_name=None, 
        phone_num=None, date_of_birth=None, country=None, state_of_origin= None, address= None,sex=None, **extra_fields)


class User(AbstractBaseUser,PermissionsMixin):
    email= models.EmailField(unique=True, max_length=254)
    first_name = models.CharField(max_length=240, null=True)
    last_name = models.CharField(max_length=240, null=True)
    phone_num = models.CharField(max_length=50, null=True)
    date_of_birth = models.CharField(max_length=50, null=True)
    sex = models.CharField(max_length=5, null=True)
    country = models.CharField(max_length=50, null=True)
    state_of_origin = models.CharField(max_length=50, null=True)
    address = models.TextField(null=True)
    is_staff = models.BooleanField(default=False)
    is_active =  models.BooleanField(default=True)
    is_superuser =  models.BooleanField(default=False)
    is_document_submitted = models.BooleanField(default=False)
    is_document_verified = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['email']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'