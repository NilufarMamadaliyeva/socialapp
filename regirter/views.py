from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken
from .serializers import RegisterSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

@api_view(['POST'])
def login(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    _,token = AuthToken.objects.create(user)

    return Response({
        "user_info":{
            'id': user.id, 
            'username': user.username, 
            'email': user.email           
        },
        "token": token
    })
@api_view(['GET'])
def get_user_info(request):
    user = request.user

    if user.is_authenticated:
        return Response({
            "user_info":{
                'id': user.id, 
                'username': user.username, 
                'email': user.email           
            }
        })
    return Response({'error': 'User is not authenticated'},status=400)


@api_view(['POST'])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()

    _,token = AuthToken.objects.create(user)

    return Response({
        "user_info":{
            'id': user.id, 
            'username': user.username, 
            'email': user.email           
        },
        "token": token
    })

