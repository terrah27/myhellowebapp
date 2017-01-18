from django.contrib import admin

# Register your models here.
from collection.models import Pharmacist

## set up automatic slug generation
class PharmacistAdmin(admin.ModelAdmin):
	model = Pharmacist
	list_display = ('name', 'description',)
	prepopulated_fields = {'slug': ('name',)}

## and register my model
admin.site.register(Pharmacist, PharmacistAdmin)
