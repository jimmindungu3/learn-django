from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from .models import User


# Home Route
def home(request):
    return JsonResponse({"Message": "Welcome home!"})


# Create User Route
@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user = User.objects.create(
                username=data.get('username'),
                email=data.get('email')
            )
            return JsonResponse({
                'id': user.id,
                'username': user.username,
                'email': user.email
            }, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid method'}, status=405)


# Get All Users Route
def get_all_users(request):
    if request.method == 'GET':
        try:
            # Query all users
            users = User.objects.all()
            
            # Serialize user data
            users_list = [
                {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email
                } for user in users
            ]
            
            # Return the data
            return JsonResponse({'users': users_list}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid method'}, status=405)


# Delete User with ID
@csrf_exempt
def delete_user(request, user_id):
    if request.method == 'DELETE':
        try:
            # Attempt to find the user
            user = User.objects.get(id=user_id)
            user.delete()  # Delete the user
            return JsonResponse({'message': f'User with ID {user_id} deleted successfully.'}, status=200)
        except User.DoesNotExist:
            return JsonResponse({'error': f'User with ID {user_id} not found.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid method'}, status=405)