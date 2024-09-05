from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .serializers import RegistrationSerializer, ConfirmationSerializer


# Регистрация пользователя
class RegisterUserView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "Регистрация прошла успешно. Проверьте email для кода подтверждения."},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Подтверждение пользователя
class ConfirmUserView(APIView):
    def post(self, request):
        serializer = ConfirmationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Подтверждение прошло успешно. Ваш аккаунт активен."},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Авторизация пользователя (получение токена)
class LoginUserView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                token, _ = Token.objects.get_or_create(user=user)
                return Response({"token": token.key}, status=status.HTTP_200_OK)
            return Response({"message": "Аккаунт не подтвержден."}, status=status.HTTP_403_FORBIDDEN)
        return Response({"message": "Неверные учетные данные."}, status=status.HTTP_400_BAD_REQUEST)
