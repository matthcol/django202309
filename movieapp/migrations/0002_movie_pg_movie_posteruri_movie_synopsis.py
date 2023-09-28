# Generated by Django 4.2.5 on 2023-09-28 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='pg',
            field=models.CharField(choices=[('X', 'X'), ('R', 'R'), ('PG_13', 'Pg 13'), ('PG', 'Pg'), ('G', 'G')], max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='posterUri',
            field=models.CharField(db_column='poster_uri', max_length=330, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='synopsis',
            field=models.CharField(max_length=5000, null=True),
        ),
    ]