from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import User

# Create your views here.
def home(request):
    return HttpResponse("Welcome To User's Home")


@csrf_exempt
def create_user(request):
    if request.method == "POST":
        try:
            # Parse the JSON request body
            user_data = json.loads(request.body)
            username = user_data.get('username')
            email = user_data.get('email')
            phone_number = user_data.get('phone_number')

            # Validate received data
            if not username or not email or not phone_number:
                return JsonResponse({"error": "Ensure all user fields are present"})
            
            # Save user to DB if valid
            new_user = User.objects.create(username=username, email=email, phone_number=phone_number)
            print("Hit")

            # Send back success message on saving user
            return JsonResponse({"Message": "User created successfully", "user": user_data}, status=201)
        
        except:
            return JsonResponse({"message": "Internal Server Error"}, status=500)
        
