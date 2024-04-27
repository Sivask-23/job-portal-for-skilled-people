from django.contrib import admin

from . models import Resume , Employe, Jobs , ApplyJob

# Register your models here.



admin.site.register(Resume)
admin.site.register(Employe)
admin.site.register(Jobs)
admin.site.register(ApplyJob)