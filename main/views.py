from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from .models import User

def hello_world(request):
    return JsonResponse({"Message": "Hello, World!"})

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