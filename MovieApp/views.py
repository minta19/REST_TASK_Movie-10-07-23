from django.shortcuts import render
from .serializers import MovieSerializer
from .models import Movie
from rest_framework import generics
from rest_framework.response import Response

# Create your views here.
class MovieCreateList(generics.ListCreateAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer

    def post(self, request, *args, **kwargs):
        response= super().post(request, *args, **kwargs)
        return Response({'message':'Movie added'})
    

class MovieUpdations(generics.RetrieveUpdateDestroyAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer


    def delete(self, request, *args, **kwargs):
        response= super().delete(request, *args, **kwargs)
        return Response({'message':'Movie deleted'})