# Generated by Django 2.0.4 on 2018-04-24 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MatrixOfYouApp', '0002_auto_20180424_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='patientViewCode',
            field=models.CharField(default='55575', max_length=5),
        ),
    ]
