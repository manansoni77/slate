from django.urls import path
from .views import (
    login,
    student_achievements,
    school_dashboard,
    parent_dashboard,
    student_dashboard,
)

urlpatterns = [
    path("auth/login", login),
    path("dashboard/school", school_dashboard),
    path("dashboard/parent", parent_dashboard),
    path("dashboard/student", student_dashboard),
    path("student/achievements/<int:student_id>", student_achievements),
]
