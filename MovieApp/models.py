from django.db import models

class Movie(models.Model):
    title=models.CharField(max_length=255)
    release_date=models.DateField()
    genre=models.CharField(max_length=100)
    duration_minutes=models.IntegerField()
    rating=models.FloatField()

    def __str__(self) -> str:
        return self.title