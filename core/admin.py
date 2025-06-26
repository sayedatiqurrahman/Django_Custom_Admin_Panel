from django.contrib import admin
from .models import Comments
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group

from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
from unfold.admin import ModelAdmin as UnfoldModelAdmin


# Register your models here.


admin.site.unregister(User)
admin.site.unregister(Group)



@admin.register(User)
class UserAdmin(BaseUserAdmin, UnfoldModelAdmin):
    # Forms loaded from `unfold.forms`
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, UnfoldModelAdmin):
    pass


@admin.register(Comments)
class CommentAdmin(UnfoldModelAdmin):
    list_display=('id', 'message')