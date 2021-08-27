from django.db import models

class Taxpayer(models.Model):

    TAXPAYER_TYPES = [
    ('IAR', 'Individual_annual_report'),
    ('EAR', 'Entreprenuer_annual_report'),
    ]

    id = models.BigIntegerField(primary_key=True)
    tfn = models.TextField(max_length=15, null=False)
    name = models.TextField(max_length=20, null=False)
    taxpayer_type = models.CharField(TAXPAYER_TYPES, max_length=3, null=False)
    source = models.TextField(max_length=30, null=True)


class IAR(models.Model):
    id = models.BigIntegerField(primary_key=True)
    tfn = models.TextField(max_length=15, null=False)
    name = models.TextField(max_length=20, null=False)
    taxpayer_year = models.TextField(max_length=4, null=False)
    gross_income = models.FloatField(null=False)
    tax_due = models.FloatField(null=False)


class EAR(models.Model):
    id = models.BigIntegerField(primary_key=True)
    tfn = models.TextField(max_length=15, null=False)
    name = models.TextField(max_length=20, null=False)
    taxpayer_year = models.TextField(max_length=4, null=False)
    gross_income = models.FloatField(null=False)
    tax_due = models.FloatField(null=False)
