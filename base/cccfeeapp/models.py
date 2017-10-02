from django.db import models
from django.contrib.auth.models import User

class Bankinfo(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    bankname = models.TextField(blank=True, null=True)
    longname = models.TextField(blank=True, null=True)
    bankcode = models.TextField(blank=True, null=True)
    countryname = models.TextField(blank=True, null=True)
    countrycode = models.TextField(blank=True, null=True)
    

    def __unicode__(self):
        return self.longname

    def __str__(self):
        return self.longname

    class Meta:
        managed = False
        db_table = 'bankinfo'



# methods
    def get_id(self):
        return self.id

    def get_name(self):
        return self.longname



class Annualbankdata(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tenor4m = models.TextField(db_column='tenor4M', blank=True, null=True)  # Field name made lowercase.
    tenor9m = models.TextField(db_column='tenor9M', blank=True, null=True)  # Field name made lowercase.
    tenor12m = models.TextField(db_column='tenor12M', blank=True, null=True)  # Field name made lowercase.
    tenor6m = models.TextField(db_column='tenor6M', blank=True, null=True)  # Field name made lowercase.
    tenor18m = models.TextField(db_column='tenor18M', blank=True, null=True)  # Field name made lowercase.
    bankcode = models.TextField(blank=True, null=True,)
    tenor3m = models.TextField(db_column='tenor3M', blank=True, null=True)  # Field name made lowercase.
    tenor15m = models.TextField(db_column='tenor15M', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'annualbankdata'


class Semibankdata(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tenor4m = models.TextField(db_column='tenor4M', blank=True, null=True)  # Field name made lowercase.
    tenor9m = models.TextField(db_column='tenor9M', blank=True, null=True)  # Field name made lowercase.
    tenor12m = models.TextField(db_column='tenor12M', blank=True, null=True)  # Field name made lowercase.
    tenor6m = models.TextField(db_column='tenor6M', blank=True, null=True)  # Field name made lowercase.
    tenor18m = models.TextField(db_column='tenor18M', blank=True, null=True)  # Field name made lowercase.
    bankcode = models.TextField(blank=True, null=True)
    tenor3m = models.TextField(db_column='tenor3M', blank=True, null=True)  # Field name made lowercase.
    tenor15m = models.TextField(db_column='tenor15M', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'semibankdata'

