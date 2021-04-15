from django.db import models
from hello_world.util import current_year
import json

# Create your models here.

class Artikal(models.Model):
    ime = models.CharField(max_length=255)
    kolicina = models.PositiveIntegerField()
    cijena_pojedinog = models.PositiveIntegerField()

    def __str__(self):
        return json.dumps({"ime":self.ime, "kolicina":self.kolicina, "cijena_pojedinacnog":self.cijena_pojedinog})


class Auto(models.Model):
    marka = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    godina_proizvodnje = models.PositiveIntegerField(default=current_year)

    def __str__(self):
        return json.dumps({"marka":self.marka, "model":self.model, "godina_proizvodnje":self.godina_proizvodnje})


class AutoZaProdaju(models.Model):
    auto = models.ForeignKey(to="Auto", on_delete=models.CASCADE)
    artikal = models.ForeignKey(to="Artikal", on_delete=models.CASCADE)

    def __str__(self):
        auto_str = str(self.auto)
        artikal_str = str(self.artikal)
        return json.dumps({"auto":auto_str, "artikal":artikal_str}).replace(r'\"', r'"')


class AutomobilskiDio(models.Model):
    opis = models.CharField(max_length=255)
    auto = models.ForeignKey(to="Auto", on_delete=models.CASCADE)
    artikal = models.ForeignKey(to="Artikal", on_delete=models.CASCADE)

    def __str__(self):
        return json.dumps({"opis": self.opis, "auto": str(self.auto), "artikal": str(self.artikal)}).replace(r'\"', r'"')


class Vlasnik(models.Model):
    ime = models.CharField(max_length=255)
    prezime = models.CharField(max_length=255)
    automobili = models.ManyToManyField(Auto)

    def __str__(self):
        return json.dumps({"ime": self.ime, "prezime": self.prezime}).replace(r'\"', r'"')


# class Vlasnik_Auto(models.Model):
#     datum = models.DateField()
#     vlasnik = models.ForeignKey(Vlasnik, on_delete=models.CASCADE)
#     auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
#
#     class Meta:
#         auto_created = True
#
#     def __str__(self):
#         return json.dumps({"auto": str(auto_str), "vlasnik": str(vlasnik)}).replace(r'\"', r'"')
#
