from django.contrib import admin
from inupgroapp.models import ClubDetails,InstructorportfolioItem,CareerCounselors,AboutUs,UserProfile,Student,Teacher,SchoolPage,ourpartners,SchoolDetails,CollegeDetails,InstitutionDetails,CareerStrategiest
# Register your models here.
# class CommonFieldsAdmin(admin.ModelAdmin):
#     list_display=['first_name','last_name','username','email','phone','date']
admin.site.register(UserProfile)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(AboutUs)
admin.site.register(SchoolPage)
admin.site.register(ourpartners)
admin.site.register(SchoolDetails)
admin.site.register(CollegeDetails)
admin.site.register(InstitutionDetails)
admin.site.register(CareerStrategiest)
admin.site.register(CareerCounselors)
admin.site.register(InstructorportfolioItem)
admin.site.register(ClubDetails)