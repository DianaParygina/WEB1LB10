from django.db import models

class Breed(models.Model):
    name = models.TextField("Название породы")

    class Meta:
        verbose_name = "Порода"
        verbose_name_plural = "Породы"

    def __str__(self) -> str:
        return self.name
    
# Create your models here.
class Dog(models.Model):
    name = models.TextField("Название")
    breed = models.ForeignKey("Breed", on_delete=models.CASCADE, null=True)
    owner = models.ForeignKey("Owner", on_delete=models.CASCADE, null=True, related_name='dogs')
    country = models.ForeignKey("Country", on_delete=models.CASCADE, null=True, related_name='dog_country')
    hobby = models.ForeignKey("Hobby", on_delete=models.CASCADE, null=True, related_name='dog_hobby')

    class Meta:
        verbose_name = "Собака"
        verbose_name_plural = "Собаки"

    def __str__(self) -> str:
        return self.name
    

class Owner(models.Model):
    first_name = models.TextField("Имя")
    last_name = models.TextField("Фамилия")
    phone_number = models.TextField("Номер телефона")

    class Meta:
        verbose_name = "Владелец"
        verbose_name_plural = "Владельцы"

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    

class Country(models.Model):
    country = models.TextField("Страна проживания")

    class Meta:
        verbose_name = "Страна проживания"
        verbose_name_plural = "Страны"

    def __str__(self) -> str:
        return f"{self.country}" 
    

class Hobby(models.Model):
    name_hobby = models.TextField("Название хобби")

    class Meta:
        verbose_name = "Хобба"
        verbose_name_plural = "Хобби"

    def __str__(self) -> str:
        return f"{self.name_hobby}"      
