from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.userMaster)
admin.site.register(models.userProfile)
admin.site.register(models.product)
admin.site.register(models.productCategory)
admin.site.register(models.orderMaster)
admin.site.register(models.orderDetails)
admin.site.register(models.complaint)
