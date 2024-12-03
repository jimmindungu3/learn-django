from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
import json
from .models import User

# Create your views here.
def home(request):
    return HttpResponse("Welcome To User's Home")

# CREATE User Route
@csrf_exempt
def create_user(request):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST method is allowed"}, status=405)

    try:
        # Parse the JSON request body
        user_data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON body"}, status=400)

    username = user_data.get('username')
    email = user_data.get('email')
    phone_number = user_data.get('phone_number')

    # Validate received data
    if not username or not email or not phone_number:
        return JsonResponse({"error": "Ensure all user fields (username, email, phone_number) are present"}, status=400)

    try:
        # Save user to DB if valid
        new_user = User.objects.create(username=username, email=email, phone_number=phone_number)
        return JsonResponse(
            {"message": "User created successfully", "user": {"username": username, "email": email, "phone_number": phone_number}}, 
            status=201
        )
    except ValidationError as e:
        return JsonResponse({"error": "Validation error", "details": str(e)}, status=400)
    except Exception as e:
        return JsonResponse({"error": "Internal Server Error", "details": str(e)}, status=500)

# DELETE User Route   
@csrf_exempt
def delete_user(request, username):
    if request.method != "DELETE":
        return JsonResponse({"error": "Only 'DELETE' method allowed"}, status=405)

    try:
        user = User.objects.get(username=username)
        user.delete()
        return JsonResponse({"message": f"User with username {username} deleted successfully"}, status=204)
    except User.DoesNotExist:
        return JsonResponse({"error": f"User with username {username} does not exist"}, status=404)
    except Exception as e:
        return JsonResponse({"error": f"An error occurred: {str(e)}"}, status=500)