from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from djrest.models import *
from djrest.serializers import kursSerializer


class KursAPIList(generics.ListCreateAPIView):
    queryset = kurs.objects.all()
    serializer_class = kursSerializer
    Permission_classes = (IsAuthenticatedOrReadOnly,)

class KursAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = kurs.objects.all()
    serializer_class = kursSerializer
    Permission_classes = (IsAuthenticatedOrReadOnly,)

class KursAPIDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = kurs.objects.all()
    serializer_class = kursSerializer
    Permission_classes = (IsAuthenticatedOrReadOnly,)