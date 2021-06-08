from django.db import models

class Driver(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    team_name = models.CharField(max_length=30)
    driver_number = models.IntegerField()
    nationality = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name

class Constructor(models.Model):
    constructor_name = models.CharField(max_length=50)
    base = models.CharField(max_length=100)
    team_chief = models.CharField(max_length=30)
    first_team_entry = models.IntegerField()
    pole_positions = models.IntegerField()

    def __str__(self):
        return self.constructor_name