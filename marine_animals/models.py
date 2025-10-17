from django.db import models

class SeaAnimal(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    species = models.CharField(max_length=100, verbose_name="Вид")
    habitat = models.CharField(max_length=100, verbose_name="Среда обитания")
    diet = models.CharField(max_length=50, verbose_name="Тип питания")
    conservation_status = models.CharField(max_length=50, verbose_name="Статус сохранения") 


    class Meta:
        verbose_name_plural = 'SeaAnimals'



class Aquarium(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    volume = models.IntegerField(verbose_name="Объем (литры)")
    water_type = models.CharField(max_length=50, verbose_name="Тип воды")
    temperature = models.DecimalField(max_digits=4, decimal_places=1, verbose_name="Температура")
    capacity = models.IntegerField(verbose_name="Вместимость животных")
     
    
    class Meta:
        verbose_name_plural = 'Aquariums'


class Employee(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    position = models.CharField(max_length=100, verbose_name="Должность")
    hire_date = models.DateField(verbose_name="Дата найма")
    phone_number = models.CharField(max_length=20, verbose_name="Телефон")

    
    class Meta:
        verbose_name_plural = 'Employees'


class Feeding(models.Model):
    animal = models.ForeignKey(SeaAnimal, on_delete=models.CASCADE, verbose_name="Животное")
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Сотрудник")
    feeding_time = models.DateTimeField(verbose_name="Время кормления")
    food_type = models.CharField(max_length=100, verbose_name="Тип корма")
    quantity = models.CharField(max_length=50, verbose_name="Количество")

    class Meta:
        verbose_name_plural = 'Employees'


class Ticket(models.Model):
    ticket_type = models.CharField(max_length=50, verbose_name="Тип билета")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Цена")
    duration = models.CharField(max_length=50, verbose_name="Продолжительность")
    includes_tour = models.BooleanField(default=False, verbose_name="Включает экскурсию")
    description = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name_plural = 'Tickets'


class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    event_date = models.DateTimeField(verbose_name="Дата и время")
    max_participants = models.IntegerField(verbose_name="Макс. участников")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Стоимость")

    class Meta:
        verbose_name_plural = 'Events'


