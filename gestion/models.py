from django.db import models

# Create your models here.

class Categoria(models.Model):
    #el id se puede crear o no crear (es obligatorio a nivel de base de fatos) pero si no lo declaramos DJANGO igual lo creara en la bd

    id = models.AutoField(primary_key=True)
    nombre = models.TextField(null=False, unique=True)
    estante = models.TextField()
    piso = models.TextField()
    habilitado = models.BooleanField(default=True)

    class Meta:
        db_table = 'categorias'
        unique_together = ['estante','piso']

class Libro(models.Model):
    titulo = models.TextField(null=False)
    fechaPublicacion = models.DateField(db_column='fecha_publicacion')
    unidades = models.IntegerField(default=0)
    sinopsis = models.TextField()
    # on_delete > sirve para indicar que va a suceder cuando se intente eliminar una categoria
    # CASCADE > eliminara la categoria y luego todos sus libros
    # PROTECT > evitara la eliminacion de la categoria mientras esta tenga libros
    # SET_NULL > eliminara la categoria y a los libros les cambiara el valor a NULL en la bd
    # SET_DEFAULT > eliminara la categoria y cambiara el valor a un valor por defecto colocado en el parametro DEFAULT
    # DO_NOTHING > elimina la categoria y no cambia el valor de la categoria a la cual pertenece el libro, NO SE RECOMIENDA UTILIZAR ESTO porque genera mala integracion de datos

    categoria = models.ForeignKey(to=Categoria,db_column='categoria_id',related_name='libros', on_delete=models.CASCADE)

    class Meta:
        db_table = 'libros'

class Autor(models.Model):
    nombre = models.TextField(null=False)
    nacionalidad = models.TextField()
    foto = models.ImageField()
    libros = models.ManyToManyField(to=Libro)

    class Meta:
        db_table = 'autores'
        unique_together = ['nombre','nacionalidad']