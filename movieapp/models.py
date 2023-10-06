from django.db import models
from django.urls import reverse

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
    duration = models.IntegerField(null=True, blank=True)
    pg = models.CharField(max_length=5, choices=Pg.choices, null=True, blank=True)
    synopsis = models.CharField(max_length=5000, null=True, blank=True)
    # NB: use models.TextField to have texte without "limit"
    posterUri = models.CharField(
        max_length=330, 
        null=True, blank=True,
        db_column="poster_uri"
    )
    
    # many to one relationship
    director = models.ForeignKey(
        Person, 
        null=True, blank=True,
        on_delete=models.DO_NOTHING,
        # db_column = "id_director",
        related_name='directedMovies'
    )

    # many to many relationship (association table transparent)
    # actors = models.ManyToManyField(
    #     Person, 
    #     related_name='playedMovies',
    #     db_table='play'
    # )

    # many to many relationship with field (association table explicit)
    actors = models.ManyToManyField(
        Person, 
        through='play',
        through_fields=('movie', 'actor'),
        related_name='playedMovies'
    )

    # url resoltion after add/edit movie
    def get_absolute_url(self):
        return reverse('movie_detail', kwargs={'id': self.pk})
        # return reverse('movie_list')

    def __repr__(self):
        return f"#{self.id} - {self.title} ({self.year})"
    
    __str__ = __repr__
    

class Play(models.Model):
    # id auto by django
    movie = models.ForeignKey(
        Movie, 
        db_column='movie_id',
        related_name='actorsWithRole',
        on_delete=models.DO_NOTHING
    )
    actor = models.ForeignKey(
        Person, 
        db_column='actor_id',
        related_name='moviesWithRole',
        on_delete=models.DO_NOTHING
    )
    role = models.CharField(max_length=150, null = True)

    class Meta:
        db_table = 'play'


    

