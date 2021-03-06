# Generated by Django 3.2.6 on 2021-08-27 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EAR',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('tfn', models.TextField(max_length=15)),
                ('name', models.TextField(max_length=20)),
                ('taxpayer_year', models.TextField(max_length=4)),
                ('gross_income', models.FloatField()),
                ('tax_due', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='IAR',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('tfn', models.TextField(max_length=15)),
                ('name', models.TextField(max_length=20)),
                ('taxpayer_year', models.TextField(max_length=4)),
                ('gross_income', models.FloatField()),
                ('tax_due', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Taxpayer',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('tfn', models.TextField(max_length=15)),
                ('name', models.TextField(max_length=20)),
                ('taxpayer_type', models.CharField(max_length=3, verbose_name=[('IAR', 'Individual_annual_report'), ('EAR', 'Entreprenuer_annual_report')])),
                ('source', models.TextField(max_length=30, null=True)),
            ],
        ),
    ]
