from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, viewsets

from dogs.models import Dog
from dogs.serializers import DogSerializer

class DogsViewset(mixins.ListModelMixin, GenericViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer