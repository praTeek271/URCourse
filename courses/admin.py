from django.contrib import admin
from courses.models import FeedBack,CustomerAccount,store_courses
# from import_export.admin import ImportExportModelAdmin
# Register your models here.

# @admin.register(FeedBack,CustomerAccount,store_courses)

admin.site.register(FeedBack)
admin.site.register(CustomerAccount)
admin.site.register(store_courses)


# class ViewAdmin(ImportExportModelAdmin):
#     pass

#---------------------------------------
# user : prateekkumar
# password : 1234


#----------------------------------
# user : root
#pasword : admin542


#----------------------------------
# user : Nikhil Maurya
#password : 12345678