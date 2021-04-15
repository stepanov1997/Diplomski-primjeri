import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

import django
django.setup()

from hello_world.models import Auto,AutoZaProdaju,AutomobilskiDio,Artikal

############## CREATE WITH FOREIGN KEY ##############
artikli = Artikal.objects.all()
print(f"Prije kreiranja artikla: {artikli}")
artikli = Artikal.objects.all()
print(f"Prije kreiranja auta: {artikli}")
auta_za_prodaju = AutoZaProdaju.objects.all()
print(f"Prije kreiranja auta za prodaju: {auta_za_prodaju}\n")

artikal = Artikal()
artikal.ime = "automobil"
artikal.cijena_pojedinog = 3000
artikal.kolicina = 1
artikal.save()

artikli = Artikal.objects.all()
print(f"Poslije kreiranja artikla: {artikli}")

auto = Auto()
auto.marka = "Skoda"
auto.model = "Fabia"
auto.godina_proizvodnje = 2004
auto.save()

auta = Auto.objects.all()
print(f"Poslije kreiranja auta: {auta}")

auto_za_prodaju = AutoZaProdaju()
auto_za_prodaju.artikal = artikal
auto_za_prodaju.auto = auto
auto_za_prodaju.save()

auta_za_prodaju = AutoZaProdaju.objects.all()
print(f"Poslije kreiranja auta za prodaju: {auta_za_prodaju}\n")

artikal.delete()
print(f"Poslije kaskadnog brisanja artikla, stanje artikala: {artikli}")
print(f"Poslije kaskadnog brisanja artikla, stanje auta: {auta}")
print(f"Poslije kaskadnog brisanja artikla, stanje auta za prodaju: {auta_za_prodaju}")

auto.delete()
print(f"Poslije brisanja auta, stanje auta: {auta}")