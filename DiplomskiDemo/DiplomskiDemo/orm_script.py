import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

import django
django.setup()

from hello_world.models import Auto,AutoZaProdaju,AutomobilskiDio,Artikal

# READ operacija je izvršena u svakom koraku sa metodom Artikal.objects.all()

############## CREATE ##############
artikli = Artikal.objects.all()
print(f"Prije kreiranja: {artikli}")
artikal = Artikal()
artikal.ime = "automobil"
artikal.cijena_pojedinog = 3000
artikal.kolicina = 1
artikal.save()
artikli = Artikal.objects.all()
print(f"Poslije kreiranja: {artikli}\n")

############## UPDATE ##############
artikli = Artikal.objects.all()
print(f"Prije ažuriranja: {artikli}")
artikal_za_izmjenu = artikli[0]
artikal_za_izmjenu.cijena_pojedinog = 3500
artikal_za_izmjenu.save()
print(f"Poslije ažuriranja: {artikli}\n")

############## DELETE ##############
artikli = Artikal.objects.all()
print(f"Prije brisanja: {artikli}")
artikal_za_izmjenu = artikli[0]
artikal_za_izmjenu.delete()
print(f"Poslije brisanja: {artikli}\n")

