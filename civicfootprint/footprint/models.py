from django.contrib.gis.db import models

class CommonInfo(models.Model):
    name = models.TextField()
    slug = models.SlugField()

    class Meta:
        abstract = True

class DistrictType(CommonInfo):
    rep_title = models.TextField()
    at_large = models.BooleanField(default=False)

class District(CommonInfo):
    dist_type = models.ForeignKey(DistrictType)
    fq_name = models.TextField() # fully-qualified name, i.e., includes type of district, eg., "Congressional District 1"
    geom = models.PolygonField()
    objects = models.GeoManager()
    
class Representative(CommonInfo):
    district = models.ForeignKey(District)
    sex = models.TextField(choices=(('M', 'Male'),
                                    ('F', 'Female')))

# Legacy models ------------------------------------------------------

class LegacyFootprint(models.Model):
    cnt_id = models.IntegerField()
    location = models.TextField()
