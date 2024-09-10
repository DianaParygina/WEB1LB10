from django.contrib import admin
from dogs.models import Vaccination, Breed, Dog, Owner, WeightEntry
# Register your models here.
@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'breed__id']

@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']    

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'phone_number']      

@admin.register(WeightEntry)
class WeightEntryAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'weight']      

@admin.register(Vaccination)
class VaccinationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'date']   
