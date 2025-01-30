from django.contrib import admin
from .models import User, StudentAchievement


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "role", "linked_student_id")
    search_fields = ("name", "email", "role")
    list_filter = ("role",)


@admin.register(StudentAchievement)
class StudentAchievementAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "school_name", "achievements")
    search_fields = ("name", "school_name")
