from django.shortcuts import render
from .serializer import RoomSerializer
from .models import Room
from rest_framework import generics


class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
