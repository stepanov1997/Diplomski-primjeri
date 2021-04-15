import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

import django

django.setup()
from hello_world.models import Auto, AutoZaProdaju, AutomobilskiDio, Artikal, Vlasnik
from django.db.models import Q
from django.db import IntegrityError
from faker import Faker

fake = Faker()
from faker_vehicle import VehicleProvider

fake.add_provider(VehicleProvider)
############## POPUNJAVANJE BAZE PODATAKA PODACIMA ##############

from django.db import transaction


@transaction.atomic
def transakcija():
    try:
        with transaction.atomic():
            for i in range(10):
                artikal = Artikal()
                artikal.ime = fake.company()
                artikal.cijena_pojedinog = fake.random.randint(1000, 10000)
                artikal.kolicina = 1
                artikal.save()

                auto = Auto()
                fake_car = fake.vehicle_object()
                auto.marka = fake_car["Make"]
                auto.model = fake_car["Model"]
                auto.godina_proizvodnje = fake_car["Year"]
                auto.save()

                if i == 5:
                    raise IntegrityError()

                auto_za_prodaju = AutoZaProdaju()
                auto_za_prodaju.artikal = artikal
                auto_za_prodaju.auto = auto
                auto_za_prodaju.save()

                vlasnik = Vlasnik()
                vlasnik.ime = fake.first_name()
                vlasnik.prezime = fake.last_name()
                vlasnik.save()

                vlasnik.automobili.add(auto)
    except IntegrityError:
        pass



number_before = Artikal.objects.count()
transakcija()
number_after = Artikal.objects.count()

print(f"Number before: {number_before}")
print(f"Number after: {number_after}")
