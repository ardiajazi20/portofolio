from django.db import models

# Create your models here.
class Sherbimet (models.Model):
    sherbimet_id = models.AutoField(primary_key=True)
    sherbimet_image = models.ImageField(upload_to="sherbime/")
    sherbimet_title = models.CharField(max_length=100, null=True, blank=True)
    sherbimet_description = models.TextField( max_length=5000, null=True, blank=True)

    def __str__(self):
        return f"{self.sherbimet_title}"

class Contact (models.Model):
    contact_id = models.AutoField(primary_key=True)
    contact_name = models.CharField(max_length=100, null=True, blank=True)
    contact_mosha = models.IntegerField(max_length=3,  null=True, blank=True)
    contact_tel = models.IntegerField(max_length=12,  null=True, blank=True)
    contact_problema = models.TextField(max_length=5000, null=True, blank=True )

    def __str__(self):
        return f'{self.contact_name}'

