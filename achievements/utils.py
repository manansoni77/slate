import jwt
import datetime
from django.conf import settings


def generate_jwt(user):
    payload = {
        "user_id": user.id,
        "role": user.role,
        "linked_student_id": (
            user.linked_student_id.student_id if user.linked_student_id else None
        ),
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=5),
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")


def decode_jwt(token):
    try:
        return jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return None
