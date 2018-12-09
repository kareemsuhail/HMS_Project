# Generated by Django 2.1.4 on 2018-12-09 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralServiceDepartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('location', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Labor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Employee')),
                ('general_service_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.GeneralServiceDepartment')),
            ],
        ),
        migrations.CreateModel(
            name='MedicalAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='MedicalDepartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('location', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalServiceDepartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('location', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalTechnican',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Employee')),
                ('medical_service_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.MedicalServiceDepartment')),
            ],
        ),
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Employee')),
                ('medical_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.MedicalDepartment')),
            ],
        ),
        migrations.CreateModel(
            name='NursingAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medical_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.MedicalDepartment')),
                ('nurse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Nurse')),
            ],
        ),
        migrations.CreateModel(
            name='Specialist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Employee')),
                ('medical_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.MedicalDepartment')),
            ],
        ),
        migrations.CreateModel(
            name='Transportation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Nurse')),
            ],
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fileId', models.IntegerField()),
                ('date_of_birth', models.DateField()),
                ('time', models.TimeField()),
                ('medical_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.MedicalDepartment')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Patient')),
            ],
        ),
        migrations.AddField(
            model_name='medicaladmin',
            name='medical_department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.MedicalDepartment'),
        ),
        migrations.AddField(
            model_name='medicaladmin',
            name='specialist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Specialist'),
        ),
    ]
