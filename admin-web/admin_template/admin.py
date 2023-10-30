from django.contrib import admin
from .models import Role, User, UserRole


class BotDBModelAdmin(admin.ModelAdmin):
    using = "admin_template"

    def save_model(self, request, obj, form, change):
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        obj.delete(using=self.using)

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        return super().formfield_for_foreignkey(
            db_field, request, using=self.using, **kwargs
        )

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        return super().formfield_for_manytomany(
            db_field, request, using=self.using, **kwargs
        )


class BotTabularInline(admin.TabularInline):
    using = "admin_template"

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        return super().formfield_for_foreignkey(
            db_field, request, using=self.using, **kwargs
        )

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        return super().formfield_for_manytomany(
            db_field, request, using=self.using, **kwargs
        )


class UserRoleInline(BotTabularInline):
    model = UserRole


@admin.register(Role)
class RoleAdmin(BotDBModelAdmin):
    inlines = (UserRoleInline,)
    list_display = ('name', )
    list_filter = ('name',)
    search_fields = ('name', )


@admin.register(User)
class UserAdmin(BotDBModelAdmin):
    inlines = (UserRoleInline,)
    list_display = ('telegram_full_name', )
    list_filter = ('telegram_full_name',)
    search_fields = ('telegram_full_name', )
