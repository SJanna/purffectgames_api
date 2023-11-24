from django.db import models

class Client(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    identification_type = models.CharField(max_length=255)
    identification_number = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    birth_date = models.DateField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Game(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    title = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image=models.URLField(max_length=2048)
    release_date = models.DateField()
    protagonist = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    productor = models.CharField(max_length=255)
    platform = models.CharField(max_length=255)
    popularity = models.FloatField()
    genre = models.CharField(max_length=255)
    rented_times = models.IntegerField(default=0)

    def __str__(self):
        return self.title + ' ' + self.platform


class Rental(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='rentals')
    games = models.ManyToManyField(Game)
    rental_date = models.DateTimeField()
    rental_deadline = models.DateTimeField()
    price = models.FloatField()