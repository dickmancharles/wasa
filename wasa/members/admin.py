from django.contrib import admin

# Register your models here.

from .models import StaffMember, StaffMemberImage, Position
from tenants.models import PropImage

class MemberAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}
	class Meta:
		model = StaffMember

admin.site.register(StaffMember, MemberAdmin)
		
class MemberImageAdmin(admin.ModelAdmin):
	class Meta:
		model = StaffMemberImage

admin.site.register(StaffMemberImage, MemberImageAdmin)

class PropImageAdmin(admin.ModelAdmin):
	class Meta:
		model = PropImage

admin.site.register(PropImage, PropImageAdmin)

class PositionAdmin(admin.ModelAdmin):
	class Meta:
		model = Position

admin.site.register(Position, PositionAdmin)
