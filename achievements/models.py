from django.db import models
import bcrypt


# Create your models here.
class StudentAchievement(models.Model):
    student_id = models.IntegerField()
    name = models.CharField(max_length=100)
    school_name = models.CharField(max_length=100)
    achievements = models.TextField()


class User(models.Model):
    ROLE_CHOICES = [("School", "School"), ("Parent", "Parent"), ("Student", "Student")]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    linked_student_id = models.ForeignKey(
        StudentAchievement, null=True, blank=True, on_delete=models.SET_NULL
    )

    def set_password(self, raw_password):
        self.password = bcrypt.hashpw(raw_password.encode(), bcrypt.gensalt()).decode()

    def check_password(self, raw_password):
        return bcrypt.checkpw(raw_password.encode(), self.password.encode())
