from django.db import models

# Create your models here.

class Caldata(models.Model):
    site = models.IntegerField(max_length=11)
    month = models.CharField(max_length=20, null=True)
    vtlid = models.IntegerField(max_length=11, null=True)
    vtlname = models.CharField(max_length=1000, null=True)
    lv1id = models.IntegerField(max_length=11, null=True)
    lv1name = models.CharField(max_length=1000, null=True)
    lv2id = models.IntegerField(max_length=11, null=True)
    lv2name = models.CharField(max_length=1000, null=True)
    lv3id = models.IntegerField(max_length=11, null=True)
    lv3name = models.CharField(max_length=1000, null=True)
    lv4id = models.IntegerField(max_length=11, null=True)
    lv4name = models.CharField(max_length=1000, null=True)
    lvleafid = models.IntegerField(max_length=11, null=True)
    lvleafname = models.CharField(max_length=1000, null=True)

    power = models.DecimalField(max_digits=16, decimal_places=2, null=True)
    bi = models.DecimalField(max_digits=32, decimal_places=16, null=True)
    gmb = models.DecimalField(max_digits=32, decimal_places=16, null=True)
    bisnr = models.DecimalField(max_digits=16, decimal_places=2, null=True)
    gmbsnr = models.DecimalField(max_digits=16, decimal_places=2, null=True)

    def __unicode__(self):
        return "{0}.{1}".format(self.site, self.month)

    class Meta:
        verbose_name = "SocialCalendar"


