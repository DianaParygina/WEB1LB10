from rest_framework import serializers

from dogs.models import Breed, Dog, Owner, Hobby, Country

class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = "__all__"


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ['id', 'first_name', 'last_name', 'phone_number']

class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields = ['id', 'name_hobby']      

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'country'] 

class DogSerializer(serializers.ModelSerializer):
    breed = BreedSerializer(read_only=True)
    owner = OwnerSerializer(read_only=True)
    weight = HobbySerializer(read_only=True)
    vac = CountrySerializer(read_only=True)

    class Meta:
        model = Dog
        fields = ['id', 'name', 'breed','owner', 'hobby', 'country']  
