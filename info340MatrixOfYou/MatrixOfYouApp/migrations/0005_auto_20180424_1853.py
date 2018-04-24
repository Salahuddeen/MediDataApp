# Generated by Django 2.0.4 on 2018-04-24 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MatrixOfYouApp', '0004_auto_20180424_1809'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointmentDate', models.DateTimeField()),
                ('reasonForVisiting', models.CharField(max_length=500)),
                ('symptoms', models.CharField(max_length=500)),
                ('doctor', models.ForeignKey(on_delete='CASCADE', to='MatrixOfYouApp.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='OTCMeds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intakeFrequency', models.CharField(choices=[('DD', 'Daily'), ('TP', 'Temporary')], default='DD', max_length=2)),
                ('medicine', models.ForeignKey(on_delete='CASCADE', to='MatrixOfYouApp.OTCMedicine')),
            ],
        ),
        migrations.CreateModel(
            name='patientIllness',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateDiagnosed', models.DateTimeField(auto_now_add=True)),
                ('dateCured', models.DateTimeField(blank=True, null=True)),
                ('ailment', models.ForeignKey(on_delete='CASCADE', to='MatrixOfYouApp.Ailments')),
            ],
        ),
        migrations.AlterField(
            model_name='patient',
            name='patientViewCode',
            field=models.CharField(default='83275', max_length=5),
        ),
        migrations.AddField(
            model_name='patientillness',
            name='patient',
            field=models.ForeignKey(on_delete='CASCADE', to='MatrixOfYouApp.Patient'),
        ),
        migrations.AddField(
            model_name='otcmeds',
            name='patient',
            field=models.ForeignKey(on_delete='CASCADE', to='MatrixOfYouApp.Patient'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(on_delete='CASCADE', to='MatrixOfYouApp.Patient'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='treatment',
            field=models.ForeignKey(on_delete='CASCADE', to='MatrixOfYouApp.Treatment'),
        ),
    ]