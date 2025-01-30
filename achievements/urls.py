from django.urls import path
from .views import (
    forgot_password,
    login,
    reset_password,
    student_achievements,
    school_dashboard,
    parent_dashboard,
    student_dashboard,
)

urlpatterns = [
    path("auth/login", login),
    path("auth/forgot_password", forgot_password),
    path("auth/reset_password", reset_password),
    path("dashboard/school", school_dashboard),
    path("dashboard/parent", parent_dashboard),
    path("dashboard/student", student_dashboard),
    path("student/achievements/<int:student_id>", student_achievements),
]
