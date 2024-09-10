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

    class Meta:
        verbose_name = "Собака"
        verbose_name_plural = "Собаки"

    def __str__(self) -> str:
        return self.name
    

class Owner(models.Model):
    first_name = models.TextField("Имя")
    last_name = models.TextField("Фамилия")
    phone_number = models.TextField("Номер телефона")
    dogs = models.ForeignKey("Dog", on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Владелец"
        verbose_name_plural = "Владельцы"

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    

class WeightEntry(models.Model):
    date = models.DateField("Дата")
    weight = models.TextField("Вес (кг)")
    dogs = models.ForeignKey("Dog", on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Запись веса"
        verbose_name_plural = "Записи веса"

    def __str__(self):
        return f"{self.weight} кг" 
    

class Vaccination(models.Model):
    name = models.TextField("Название прививки")
    date = models.DateField("Дата прививки")
    dogs = models.ForeignKey("Dog", on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Прививка"
        verbose_name_plural = "Прививки"

    def __str__(self):
        return f"{self.name}"      
