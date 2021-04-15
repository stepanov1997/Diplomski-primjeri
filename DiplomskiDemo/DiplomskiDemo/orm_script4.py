import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

import django

django.setup()

from hello_world.models import Auto, AutoZaProdaju, AutomobilskiDio, Artikal, Vlasnik
from django.db.models import Q

from faker import Faker
fake = Faker()
from faker_vehicle import VehicleProvider
fake.add_provider(VehicleProvider)
############## POPUNJAVANJE BAZE PODATAKA PODACIMA ##############
for _ in range(10):
    artikal = Artikal()
    artikal.ime = fake.company()
    artikal.cijena_pojedinog = fake.random.randint(1000,10000)
    artikal.kolicina = 1
    artikal.save()

    auto = Auto()
    fake_car = fake.vehicle_object()
    auto.marka = fake_car["Make"]
    auto.model = fake_car["Model"]
    auto.godina_proizvodnje = fake_car["Year"]
    auto.save()

    auto_za_prodaju = AutoZaProdaju()
    auto_za_prodaju.artikal = artikal
    auto_za_prodaju.auto = auto
    auto_za_prodaju.save()

    vlasnik = Vlasnik()
    vlasnik.ime = fake.first_name()
    vlasnik.prezime = fake.last_name()
    vlasnik.save()

    vlasnik.automobili.add(auto)

data = AutoZaProdaju.objects.filter(artikal__ime__istartswith="sm").order_by("artikal__ime")
data = [(elem.artikal.ime, elem.auto.marka, elem.auto.model) for elem in data]
print("Auta za prodaju čije ime artikla počinje na SM sortirani po imenu artikla:")
for elem in data[:5]:
    print(elem)
print()

data = Artikal.objects.filter(Q(cijena_pojedinog__gte=4000) & Q(cijena_pojedinog__lte=6000)).order_by("ime")
data = [(elem.ime, elem.cijena_pojedinog) for elem in data]
print("Artikli koji koštaju između 4000 i 6000 KM sortirani po imenu:")
for elem in data[:5]:
    print(elem)
print()

data = Vlasnik.automobili.through.objects.filter(vlasnik__automobili__marka__iexact="BMW").order_by("vlasnik__ime")
data = [(elem.vlasnik.ime, elem.auto) for elem in data]
print("Vlasnici koji među svojim automobilima imaju BMW-a, sortirani po imenu:")
for elem in data[:5]:
    print(elem)
