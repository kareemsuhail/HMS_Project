from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    employment_date = models.DateField()
    salary = models.IntegerField()
    def __str__(self):
        return self.first_name + " " + self.last_name
class Patient(models.Model):
    gender_choices = (('M',"Male"),('F',"Female"))
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender =  models.CharField(max_length=1, choices=gender_choices)
    date_of_birth = models.DateField()
    def __str__(self):
        return self.first_name + " " + self.last_name
class MedicalDepartment(models.Model):
    name = models.CharField(max_length=40)
    location = models.CharField(max_length=40)
    def __str__(self):
        return self.name
class MedicalServiceDepartment(models.Model):
    name = models.CharField(max_length=40)
    location = models.CharField(max_length=40)
    def __str__(self):
        return self.name
class GeneralServiceDepartment(models.Model):
    name = models.CharField(max_length=40)
    location = models.CharField(max_length=40)
    def __str__(self):
        return self.name
class Specialist(models.Model):
    employee = models.ForeignKey('Employee',on_delete=models.CASCADE)
    medical_department = models.ForeignKey('MedicalDepartment',on_delete=models.CASCADE)
    def __str__(self):
        return self.employee.first_name + " " +self.employee.last_name
class MedicalAdmin(models.Model):
    specialist = models.ForeignKey('Specialist',on_delete=models.CASCADE)
    medical_department = models.ForeignKey('MedicalDepartment',on_delete=models.CASCADE)
    def __str__(self):
        return self.medical_department.name
class Treatment(models.Model):
    patient = models.ForeignKey('Patient',on_delete=models.CASCADE)
    medical_department =models.ForeignKey('MedicalDepartment',on_delete=models.CASCADE)
    fileId = models.IntegerField()
    date_of_birth = models.DateField()
    time = models.TimeField()
    def __str__(self):
        return self.patient.first_name + " " + self.patient.last_name
class Nurse(models.Model):
    employee = models.ForeignKey('Employee',on_delete=models.CASCADE)
    medical_department = models.ForeignKey('MedicalDepartment',on_delete=models.CASCADE)
    def __str__(self):
        return self.employee.first_name + " " +self.employee.last_name
class NursingAdmin(models.Model):
    nurse = models.ForeignKey('Nurse',on_delete=models.CASCADE)
    medical_department = models.ForeignKey('MedicalDepartment',on_delete=models.CASCADE)
    def __str__(self):
        return self.nurse.employee.first_name + " " +self.employee.last_name
class Labor(models.Model):
    employee = models.ForeignKey('Employee',on_delete=models.CASCADE)
    general_service_department = models.ForeignKey('GeneralServiceDepartment',on_delete=models.CASCADE)
    def __str__(self):
        return self.employee.first_name + " " + self.employee.last_name
class MedicalTechnican(models.Model):
    employee = models.ForeignKey('Employee',on_delete=models.CASCADE)
    medical_service_department = models.ForeignKey('MedicalServiceDepartment',on_delete=models.CASCADE)
    def __str__(self):
        return self.employee.first_name + " " + self.employee.last_name
class Transportation(models.Model):
    type = models.CharField(max_length=30)
    driver = models.ForeignKey('Nurse',on_delete=models.CASCADE)
    def __str__(self):
        return self.driver.employee.first_name + " " + self.employee.last_name
