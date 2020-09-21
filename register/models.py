from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)

class UserManager(BaseUserManager):
    def create_user(self, mobile, password=None):
        """
        Creates and saves a User with the given mobile, date of
        birth and password.
        """
        if not mobile:
            raise ValueError('Users must have an mobile no')

        user = self.model(
            mobile=mobile,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, mobile, password=None):
        """
        Creates and saves a superuser with the given mobile, date of
        birth and password.
        """
        user = self.create_user(
            mobile,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    mobile      = models.CharField(unique=True, max_length=15)
    is_admin       = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)
    is_driver = models.BooleanField(default=False)

    USERNAME_FIELD = 'mobile' #username

    REQUIRED_FIELDS = []

    objects = UserManager()
    def __str__(self):
        return str(self.mobile)

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
        # Simplest possible answer: All admins are staff
        return self.is_admin