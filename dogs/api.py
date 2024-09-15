from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, viewsets

from dogs.models import Breed, Dog, Owner, Country, Hobby
from dogs.serializers import DogSerializer, BreedSerializer, OwnerSerializer, CountrySerializer, HobbySerializer

class DogsViewset(
    mixins.CreateModelMixin, 
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer


class BreedsViewset(
    mixins.CreateModelMixin, 
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class OwnersViewset(
    mixins.CreateModelMixin, 
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class CountryViewset(
    mixins.CreateModelMixin, 
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class HobbyViewset(
    mixins.CreateModelMixin, 
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet):
    queryset = Hobby.objects.all()
    serializer_class = HobbySerializer