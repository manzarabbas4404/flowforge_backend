from django.contrib import admin
from organization.models import Organization, OrganizationDisplay, OrganizationMember

# Register your models here.


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("uuid", "name", "slug", "created_at", "updated_at")

    def uuid(self, obj):
        print(obj)
        return str(obj.id)

    uuid.short_description = "UUID"


class OrganizationDisplayAdmin(admin.ModelAdmin):
    list_display = ("name", "short_name", "created_at")


class OrganizationDisplayAdmin(admin.ModelAdmin):
    list_display = ("name", "short_name", "created_at")


class OrganizationMemberAdmin(admin.ModelAdmin):
    list_display = ("user", "organization", "role", "joined_at")


admin.site.register(Organization, OrganizationAdmin)
admin.site.register(OrganizationDisplay, OrganizationDisplayAdmin)
admin.site.register(OrganizationMember, OrganizationMemberAdmin)
