from django.contrib import admin

# Register your models here.
from .models import Resume, Document, GenericImage

class ResumeAdmin(admin.ModelAdmin):
	class Meta:
		model = Resume

admin.site.register(Resume, ResumeAdmin)
		
class DocumentAdmin(admin.ModelAdmin):
	class Meta:
		model = Document

admin.site.register(Document, DocumentAdmin)

class GenericImageAdmin(admin.ModelAdmin):
	class Meta:
		model = GenericImage

admin.site.register(GenericImage, GenericImageAdmin)

from django.contrib import admin


