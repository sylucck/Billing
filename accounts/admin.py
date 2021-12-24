from django.contrib import admin
from django.contrib.auth import get_user_model
from .forms import UserAdminChangeForm, RegisterForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.
CustomUser = get_user_model()


#class CustomUserAdmin(admin.ModelAdmin):
 #   search_fields = ['email']
  #  form = UserAdminChangeForm #update view
   # add_form = UserAdminCreationForm #create view
    #class Meta:
     #   model = CustomUser

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = RegisterForm
    model = CustomUser

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['email','staff', 'superuser' ]
    list_filter = ['superuser', 'staff', 'active']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name',)}),
        ('Permissions', {'fields': ('superuser','staff', 'active', )}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'password_2')}
        ),
    )
    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = ()


admin.site.register(CustomUser, UserAdmin)


#admin.site.register(CustomUser, CustomUserAdmin)