from django.db import models

# Create your models here.
class Person(models.Model):

    # customize db table
    class Meta:
        db_table = "person"

    # columns

    # explicit key: other name than id or long|small int type
    # id = models.IntegerField(primary_key=True) // do not generate pk
    id = models.AutoField(primary_key=True) # pk int auto generated (see also BigAutoField, SmallAutoField)
    name = models.CharField(max_length=150)
    birthdate = models.DateField(null=True)

    def __repr__(self):
        return f"#{self.id} - {self.name}"

    __str__ = __repr__

class Movie(models.Model):

    class Pg(models.TextChoices):
        X = 'X'
        R = 'R'
        PG_13 = 'PG_13'
        PG = 'PG'
        G = 'G'

    # id implicitly created
    title = models.CharField(max_length=250)
    year = models.IntegerField()
    duration = models.IntegerField(null=True)
    pg = models.CharField(max_length=5, choices=Pg.choices, null=True)
    synopsis = models.CharField(max_length=5000, null=True)
    posterUri = models.CharField(
        max_length=330, 
        null=True,
        db_column="poster_uri"
    )
    director = models.ForeignKey(
        Person, 
        null=True,
        on_delete=models.DO_NOTHING,
        # db_column = "id_director"
    )

    def __repr__(self):
        return f"#{self.id} - {self.title} ({self.year})"
    
    __str__ = __repr__
    

