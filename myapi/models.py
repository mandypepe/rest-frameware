from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin,BaseUserManager

# Create your models here.
class UserProfileManager(BaseUserManager):
    """Ayudar a django para trabajar con mi user model"""
    def create_user(self,email,name,password=None):
        """create new profile obj"""
        if not email:
            raise ValueError("El usuario teiene que tener un email")
        email=self.normalize_email(email)
        user=self.model(email=email,name=name)
        user.set_password(password)
        user.save(using=self._db) # usera la misma basedato configurada
        return user
    def create_superuser(self,email,name,password):
        """create an salvar un superuser con detalles"""
        user=self.create_user(email,name,password)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)
        return user




class UserProfile(AbstractBaseUser,PermissionsMixin):
    """el perfil de usuario dentro del sistema"""

    email=models.EmailField(max_length=255, unique= True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff=models.BooleanField(default=True)



    object=UserProfileManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """"Usando para get usrt full name"""
        return self.name

    def get_short_name(self):
        """Get short name"""
        return  self.name

    def __str__(self):
        """Django lo usa pa converter obj a str """
        return self.email