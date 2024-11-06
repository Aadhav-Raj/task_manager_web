from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin, UserAdmin
from django.contrib.auth.models import Group
from .models import User, Task
#from .forms import SignupForm,CustomUserChangeForm
from .forms import SignupForm,CustomUserChangeForm
class UserAdmin(UserAdmin):

    add_form=SignupForm
    form=CustomUserChangeForm
    model=User
    # The forms to add and change user instances
    list_display = ('email','username', 'first_name', 'last_name', 'is_staff',)
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name','username', 'last_name', 'gender', 'occupation', 'phone_number')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser',"groups")}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username','first_name', 'last_name', 'gender', 'occupation', 'phone_number', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'first_name', 'last_name','username')
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
#admin.site.unregister(Group)  # Optional: Unregister the Group model from the admin if you're not using it

class TaskAdmin(admin.ModelAdmin):
    list_display = ('head', 'desc', 'completed', 'user')
    list_filter = ('completed', 'user')
    search_fields = ('head', 'desc')

admin.site.register(Task, TaskAdmin)
