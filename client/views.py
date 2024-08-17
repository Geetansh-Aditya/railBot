from django.shortcuts import render
import json
import requests
from django.http import JsonResponse


# Create your views here.
def index(request):
    return render(request, 'client/index.html')


# def send_message(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         user_message = data.get('message', '')
#
#         # Process the message here, e.g., pass it to the chatbot logic
#         # For now, we just return a simple response for testing
#         bot_response = f"Echo: {user_message}"
#
#         return JsonResponse({'reply': bot_response})
#
#     return JsonResponse({'error': 'Invalid request'}, status=400)

def send_message(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data.get('message', '')

        # Send the message to the FastAPI chatbot service
        response = requests.post('http://127.0.0.1:8001/chatbot/', json={'message': user_message})
        bot_reply = response.json().get('reply', 'Sorry, I did not understand that.')

        return JsonResponse({'reply': bot_reply})

    return JsonResponse({'error': 'Invalid request'}, status=400)