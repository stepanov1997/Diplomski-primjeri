import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

import django

django.setup()

from hello_world.models import Auto, AutoZaProdaju, AutomobilskiDio, Artikal, Vlasnik

############## CREATE WITH MANY-TO-MANY REL ##############
artikal = Artikal()
artikal.ime = "automobil"
artikal.cijena_pojedinog = 3000
artikal.kolicina = 1
artikal.save()

auto = Auto()
auto.marka = "Skoda"
auto.model = "Fabia"
auto.godina_proizvodnje = 2004
auto.save()

vlasnik = Vlasnik()
vlasnik.ime = "Kristijan"
vlasnik.prezime = "Stepanov"
vlasnik.save()

vlasnik.automobili.add(auto)

print(vlasnik.automobili.all())

artikal.delete()
auto.delete()
vlasnik.delete()
