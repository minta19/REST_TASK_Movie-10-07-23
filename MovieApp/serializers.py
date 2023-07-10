from rest_framework import serializers
from .models import Movie
from rest_framework.validators import UniqueValidator
from datetime import date,timedelta
from django.core.validators import MinLengthValidator,MaxLengthValidator,MinValueValidator,MaxValueValidator

class MovieSerializer(serializers.ModelSerializer):
    title=serializers.CharField(required=True, validators=[UniqueValidator(queryset=Movie.objects.all()),
                                            MaxLengthValidator(106,message='Title can have maximum 100 characters')
                                            ])

    release_date=serializers.DateField(required=True)
    genre=serializers.CharField(required=True)
    duration_minutes=serializers.IntegerField(required=True,validators=[
        MinValueValidator(1,message='Minimum duration need to be 1 minute'),
        MaxValueValidator(600,message='Maximum duration allowed is 600 minutes')
        ])
    rating=serializers.FloatField(validators=[
        MaxValueValidator(10,message='maximum rating allowed is 10'),
        MinValueValidator(0,message='Minimum rating is zero')
        ])
    def validate_title(self, data):
        prefix='Movie-'
        if not data.startswith(prefix):
            raise serializers.ValidationError('Title must start with the prefix "Movie-"')
        value=data[len(prefix):]
        min_length_validator=MinLengthValidator(2,message='Title must  contain atleast 2 characters')
        min_length_validator(value)
        return data
   
    def validate_release_date(self, data):
        today=date.today()
        if data > today :
            raise serializers.ValidationError('No future dates are allowed')
        allowed_date=today.replace(year=date.today().year-30)
        if allowed_date > data:
            raise serializers.ValidationError('minimum allowed date is till the year 1993')
        return data
    
    def validate_genre(self, data):
        genre_choices=['Action','Drama','Comedy','Thriller','Sci-Fi']
        if data not in genre_choices:
            raise serializers.ValidationError("Invalid choice of genre select from 'Action','Drama','Comedy','Thriller','Sci-Fi'")
        
        return data


        
    class Meta:
        model=Movie
        fields='__all__'