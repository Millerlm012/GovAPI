from django.db import models

# Create your models here.
class Governor(models.Model):
    state = models.CharField(max_length=60, null=True)
    gov_Name = models.CharField(max_length=60)
    address = models.CharField(max_length=60, null=True)
    phone_Number = models.CharField(max_length=60, null=True)
    fax = models.CharField(max_length=60, null=True)
    media_Contact = models.CharField(max_length=60, null=True)
    state_Federal_Contact = models.CharField(max_length=60, null=True)
    gov_Website = models.CharField(max_length=60, null=True)
    gov_Bio = models.CharField(max_length=60, null=True)
    state_Website = models.CharField(max_length=60, null=True)
    coronavirues_Resources = models.CharField(max_length=60, null=True)

    def __str__(self):
        return self.state
