from django.db import models

class Marka(models.Model):
    Nazwa_marki =models.CharField(max_length=100)
    logo= models.ImageField(upload_to='iamges')
    utworzono = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.Nazwa_marki
    
class Typ(models.Model):
    Typ_roweru = models.CharField(max_length=100)
    utworzono = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.Typ_roweru
    

class Osprzęt(models.Model):
    Konfiguracja_osprzętu = models.CharField(max_length=100)
    Materiał_ramy = models.CharField(max_length=100)
    Widelec = models.CharField(max_length=100)
    Damper = models.CharField(max_length=100)
    Przerzutki = models.CharField(max_length=100)
    Opony = models.CharField(max_length=100)


def __str__(self):
    return self.Konfiguracja_osprzętu

class Model(models.Model):
    Model_roweru= models.CharField(max_length=100)
    osprzęt = models.ManyToManyField(Osprzęt)
    Typ = models.ManyToManyField(Typ)
    utworzono = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.Model_roweru
    





    


