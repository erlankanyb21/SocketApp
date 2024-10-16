from rest_framework.views import APIView
from rest_framework.response import Response
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class SendMessageAPI(APIView):
    def post(self, request):
        room = request.data.get('room')
        username = request.data.get('username')
        message = request.data.get('message')
        
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f'chat_{room}',
            {
                'type': 'chat_message',
                'message': message,
                'username': username
            }
        )
        
        return Response({"status": "Message sent"})

