from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin, BaseUserManager
from django.utils.html import mark_safe

# Create your models here.
class Imagen(models.Model):
    nombre = models.TextField()
    ubicacion = models.ImageField()
    
    def __str__(self):
        return self.nombre

    def ubicacion_tag(self):
        return mark_safe('<img src="/imagenes/%s" width="150" heigth="150"/>' %(self.ubicacion))
    
    ubicacion_tag.short_description = 'Imagen de la ubicacion'

    class Meta:
        db_table = 'imagenes'
        verbose_name_plural = 'Imagenes'

class Categoria(models.Model):
    nombre = models.TextField()
    imagen = models.OneToOneField(to=Imagen, on_delete=models.RESTRICT, db_column='imagen_id')

    class Meta:
        db_table = 'categorias'

class Producto(models.Model):
    nombre = models.TextField()
    fechaVencimiento = models.DateField(db_column='fecha_vencimiento')
    lote = models.TextField(null=False)
    precio = models.FloatField(null=False)
    categoria =  models.ForeignKey(to=Categoria, on_delete=models.CASCADE, db_column='categoria_id',related_name='productos')
    imagen = models.OneToOneField(to=Imagen, on_delete=models.RESTRICT, db_column='imagen_id', related_name='producto')

    class Meta:
        db_table = 'productos'

        ordering = ['nombre', '-fechaVencimiento']

class ManejoUsuario(BaseUserManager):
    def create_superuser(self,  nombre, apellido, email, password, tipo):
        if not email:
            raise ValueError('El correo es obligatorio')
        
        emailNormalizado = self.normalize_email(email)
        nuevoUsuario = self.model(email=emailNormalizado,nombre=nombre, tipo = tipo, apellido = apellido)
        
        nuevoUsuario.set_password(password)

        nuevoUsuario.save()

class Usuario(AbstractBaseUser, PermissionsMixin):
    nombre= models.TextField(null=False)
    apellido = models.TextField(null=False)
    email = models.EmailField(unique=True, null=False)
    password = models.TextField(null=False)
    tipo = models.TextField(choices=[('ADMIN','ADMIN'),('CAJERO','CAJERO')])
    is_staff = models.BooleanField(default=False, db_column='is_staff')

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['nombre','apellido','tipo']

    objects = ManejoUsuario()

    class Meta:
        db_table = 'usuarios'

