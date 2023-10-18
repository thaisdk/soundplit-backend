from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import serializers, status
from django.contrib.auth import login
from rest_framework.authtoken.models import Token
from base.models import User
from .serializers import UserSerializer


@api_view(['GET'])
def get_all_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
