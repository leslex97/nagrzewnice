from django.db import models
import datetime

class DeviceType(models.Model):
    name = models.CharField(max_length=60 , default="1", blank = True,null=True)



    def __str__(self):
        return self.name   
    
    class Meta:
        verbose_name = "Typ Urządzeń"
        verbose_name_plural = "Typy Urządzeń"
    

class Switches(models.Model):
    switch_name = models.CharField(max_length=9, default = '')
    switch_model = models.CharField(max_length=30, null = True)
    switch_place = models.CharField(max_length=12 ,default = '')
    switch_ip = models.CharField(max_length=16 ,default = '1')

    def __str__(self):
        return self.switch_name


    class Meta:
        verbose_name = "Przełącznik"
        verbose_name_plural = "Przełączniki"

class Device(models.Model):
    IMBIS_CHOICES = [("T", "Jest w Imbisie"), ("N", "Nie ma w imbisie")]
    name = models.CharField(max_length=100)
    type = models.ForeignKey(DeviceType, null=True, blank = True, on_delete=models.CASCADE, default='')
    imbis = models.CharField(max_length=1, choices=IMBIS_CHOICES)
    place = models.CharField(max_length=30)
    iP = models.CharField(max_length=16)
    mac_address = models.CharField(max_length=17)
    description = models.TextField()
    edit_date = models.DateField(default = datetime.datetime.now)
    switch = models.ForeignKey(Switches, null=True, on_delete=models.CASCADE)
    switch_port = models.CharField(max_length=2, null=True, default="")

    def __str__(self):
        return self.name   
    


    class Meta:
        verbose_name = "Urządzenie"
        verbose_name_plural = "Urządzenia"



