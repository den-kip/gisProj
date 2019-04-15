import os
from django.contrib.gis.gdal import DataSource
from django.contrib.gis.db import models #imports gis models
from django.contrib.gis.geos import Point
from postgres_copy import CopyManager
# from django.db import models

# Create your models here.
class Projects(models.Model):
    name = models.CharField(max_length = 25)
    project_name = models.CharField(max_length = 30)
    donor = models.CharField(max_length = 30)
    project_description =models.CharField(max_length = 30)
    location = models.PointField(srid = 4326)#WGS84 CODE
    #objects = gismodels.GeoManager()
    #will contain the different values in database

    def __str__(self):
        return self.name



class Subcounties(models.Model):
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    adm2_en = models.CharField(max_length=50)
    adm2_pcode = models.CharField(max_length=50)
    #adm2_ref = models.CharField(max_length=50)
    #adm2alt1en = models.CharField(max_length=50)
    #adm2alt2en = models.CharField(max_length=50)
    adm1_en = models.CharField(max_length=50)
    adm1_pcode = models.CharField(max_length=50)
    adm0_en = models.CharField(max_length=50)
    adm0_pcode = models.CharField(max_length=50)
    date = models.DateField()
    validon = models.DateField()
    #validto = models.DateField()
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.adm2_en


class Ngoprojs(models.Model):
    project_id = models.FloatField(max_length=20, null=True)
    project_na = models.CharField(max_length=200)
    org_interv = models.FloatField(max_length=50)
    donor_id = models.FloatField(max_length=50)
    sectors_ID = models.FloatField(max_length=50)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50)
    lat = models.FloatField()
    lon = models.FloatField(null=True)
    Geographic = models.CharField(max_length=50)
    budget_num = models.FloatField(max_length=50)
    budget_cur = models.CharField(max_length=50)
    geom = models.PointField(srid=4326)

    def __str__(self):
        return self.project_na


class AOF(models.Model):
    SECTOR_ID = models.FloatField(max_length=50)
    SECTOR_NAME = models.CharField(max_length=50)
    objects = CopyManager()

    def __str__(self):
        return self.SECTOR_NAME


class INSTITUTIONS(models.Model):
    INSTITUTION_ID = models.FloatField(max_length=50)
    NAME = models.CharField(max_length=50)
    CONTACT = models.CharField(max_length=50)
    objects = CopyManager()

    def __str__(self):
        return self.NAME


class NGO(models.Model):
    NGO_ID = models.FloatField(max_length=50)
    NGO_NAME = models.CharField(max_length=50)
    SECTOR_ID = models.ForeignKey(AOF, on_delete=models.CASCADE)
    INSTIT_ID = models.ForeignKey(INSTITUTIONS, on_delete=models.CASCADE)
    Contact = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    lat = models.FloatField()
    lon = models.FloatField(null=True)
    geom = models.PointField(srid=4326)

    def __str__(self):
        return self.NGO_NAME



class DONOR(models.Model):
    DONOR_ID = models.FloatField(max_length=50)
    NAME = models.CharField(max_length=50)
    NGO_ID = models.ForeignKey(NGO, on_delete=models.CASCADE)
    objects = CopyManager()

    def __str__(self):
        return self.NAME
