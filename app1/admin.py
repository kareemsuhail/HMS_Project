from django.contrib import admin
from .models import Patient,Employee,Treatment,MedicalDepartment
from .models import MedicalServiceDepartment,GeneralServiceDepartment
from .models import MedicalTechnican,Labor,Nurse,NursingAdmin,Transportation
from .models import Specialist,MedicalAdmin
# Register your models here.
admin.site.site_header = "Hospital Management system"
admin.site.index_title = "HMS administration"
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ["first_name","last_name","gender","date_of_birth"]
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["first_name","last_name","employment_date","date_of_birth","salary"]
@admin.register(MedicalDepartment)
class MedicalDepartmentAdmin(admin.ModelAdmin):
    list_display = ["name","location"]
@admin.register(MedicalServiceDepartment)
class MedicalServiceDepartmentAdmin(admin.ModelAdmin):
    list_display = ["name","location"]
@admin.register(GeneralServiceDepartment)
class GeneralServiceDepartmentAdmin(admin.ModelAdmin):
    list_display = ["name","location"]
@admin.register(Specialist)
class Specialist(admin.ModelAdmin):
    list_display = ["employee","medical_department"]
@admin.register(MedicalAdmin)
class MedicalAdminAdmin(admin.ModelAdmin):
    list_display = ["specialist","medical_department"]
@admin.register(Treatment)
class TreatmentAdmin(admin.ModelAdmin):
    list_display = ["patient","medical_department","fileId","date_of_birth","time"]
@admin.register(Nurse)
class NurseAdmin(admin.ModelAdmin):
    list_display = ["employee","medical_department"]
@admin.register(NursingAdmin)
class MedicalDepartmentadmin(admin.ModelAdmin):
    list_display = ["nurse","medical_department"]
@admin.register(Labor)
class LaborAdmin(admin.ModelAdmin):
    list_display = ["employee","general_service_department"]
@admin.register(MedicalTechnican)
class MEdicalTechnicanAdmin(admin.ModelAdmin):
    list_display = ["employee","medical_service_department"]
@admin.register(Transportation)
class TrasportationAdmin(admin.ModelAdmin):
    list_display = ["type","driver"]
