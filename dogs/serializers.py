from rest_framework import serializers

from dogs.models import Breed, Dog, Owner, WeightEntry, Vaccination

class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = "__all__"

class DogSerializer(serializers.ModelSerializer):
    breed = BreedSerializer()

    class Meta:
        model = Dog
        fields = ['id', 'name', 'breed']

class OwnerSerializer(serializers.ModelSerializer):
    owner = DogSerializer()

    class Meta:
        model = Owner
        fields = ['id', 'first_name', 'last_name', 'phone_number']

class WeightEntrySerializer(serializers.ModelSerializer):
    weight = DogSerializer()

    class Meta:
        model = WeightEntry
        fields = ['id', 'date', 'weight']      

class VaccinationSerializer(serializers.ModelSerializer):
    vac = DogSerializer()

    class Meta:
        model = Vaccination
        fields = ['id', 'name', 'date']   
