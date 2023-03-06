from django.db import models

# Create your models here.
class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    state = models.BooleanField('Estado', default=True)
    create_date = models.DateField('Fecha de creacion', auto_now=False, auto_now_add=True)
    modified_date = models.DateField('Fecha de modificacion', auto_now=True, auto_now_add=False)
    deleted_date = models.DateField('Fecha de eliminacion', auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True
        verbose_name = 'Modelo Base'
        verbose_name_plural = 'Modelos Base'
    
    def __str__(self) -> str:
        return str(self.id)

        
class BasePerson(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="name", max_length=50, null=False, blank=False)
    last_name = models.CharField(verbose_name="apellidos", max_length=50, null=False, blank=False)
    document_number = models.CharField(verbose_name="documento", max_length=20, null=False, blank=False)
    document_type = models.CharField(verbose_name="documento_type", max_length=10, null=False, blank=False)
    phone = models.CharField(verbose_name="Telefono", max_length=20, null=False, blank=False)
    email = models.EmailField()

    class Meta:
        abstract = True
        verbose_name = 'Modelo Base Person'
        verbose_name_plural = "Modelos Base Person"

    def __str__(self) -> str:
        return self.name
