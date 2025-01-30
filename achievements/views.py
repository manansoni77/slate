from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import User, StudentAchievement
from .utils import generate_jwt
from .middleware import jwt_required


@csrf_exempt
def login(request):
    if request.method == "POST":
        data = json.loads(request.body)
        email = data.get("email")
        password = data.get("password")

        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                token = generate_jwt(user)

                return JsonResponse(
                    {"token": token, "redirectUrl": f"/dashboard/{user.role.lower()}"},
                    status=200,
                )
        except User.DoesNotExist:
            return JsonResponse({"error": "User does not exist"}, status=400)

        return JsonResponse({"error": "Invalid credentials"}, status=400)

    return JsonResponse({"error": "Invalid request"}, status=405)


@jwt_required
def school_dashboard(request):
    user_data = request.user_data
    user = User.objects.get(id=user_data["user_id"])
    if user.role != "School":
        return JsonResponse({"error": "Access denied"}, status=403)

    return JsonResponse({"message": f"Welcome to the School Dashboard, {user.name}"})


@jwt_required
def parent_dashboard(request):
    user_data = request.user_data
    user = User.objects.get(id=user_data["user_id"])
    if user.role != "Parent":
        return JsonResponse({"error": "Access denied"}, status=403)

    return JsonResponse({"message": f"Welcome to the Parent Dashboard, {user.name}"})


@jwt_required
def student_dashboard(request):
    user_data = request.user_data
    user = User.objects.get(id=user_data["user_id"])
    if user.role != "Student":
        return JsonResponse({"error": "Access denied"}, status=403)

    return JsonResponse({"message": f"Welcome to the Student Dashboard, {user.name}"})


@jwt_required
def student_achievements(request, student_id):
    user_data = request.user_data

    # Allow only students & parents (linked to student_id)
    if (
        user_data["role"] not in ["Parent", "Student"]
        or user_data["linked_student_id"] != student_id
    ):
        return JsonResponse({"error": "Access denied"}, status=403)

    achievements = StudentAchievement.objects.filter(student_id=student_id).values()
    return JsonResponse({"achievements": list(achievements)})
