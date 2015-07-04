from django.db import models

# Create your models here.

# Create your models here.
class DataFile(models.Model):
    #data file type enums
    TYPE_CVS = 'CVS'
    TYPE_JSON = 'JSON'
    TYPE_XML = 'XML'
    TYPE_TXT = 'TXT'
    
    DATA_FILE_TYPES = (
        (TYPE_CVS, 'CVS'),
        (TYPE_JSON, 'JSON'),
        (TYPE_XML, 'XML'),
        (TYPE_TXT, 'TXT'),
    )

    class Meta:
        verbose_name = "DataFile"