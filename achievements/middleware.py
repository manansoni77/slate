from django.http import JsonResponse
from .utils import decode_jwt


def jwt_required(view_func):
    def wrapper(request, *args, **kwargs):
        token = request.headers.get("Authorization")
        if not token or not token.startswith("Bearer "):
            return JsonResponse({"error": "Unauthorized"}, status=401)

        decoded = decode_jwt(token[7:])
        if not decoded:
            return JsonResponse({"error": "Invalid token"}, status=401)

        request.user_data = decoded
        return view_func(request, *args, **kwargs)

    return wrapper
