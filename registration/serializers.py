from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import ConfirmationCode

User = get_user_model()

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        # Генерация кода подтверждения
        confirmation_code = ConfirmationCode.objects.create(user=user)
        confirmation_code.generate_code()
        confirmation_code.save()

        # Можно отправить код на почту
        # send_email(user.email, confirmation_code.code)

        return user


class ConfirmationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField(max_length=6)

    def validate(self, data):
        email = data.get('email')
        code = data.get('code')
        try:
            user = User.objects.get(email=email)
            confirmation_code = ConfirmationCode.objects.get(user=user, code=code)
        except User.DoesNotExist:
            raise serializers.ValidationError("Пользователь с таким email не найден.")
        except ConfirmationCode.DoesNotExist:
            raise serializers.ValidationError("Неправильный код подтверждения.")
        return data

    def save(self, **kwargs):
        email = self.validated_data['email']
        user = User.objects.get(email=email)
        user.is_active = True  # Активируем пользователя
        user.save()
        ConfirmationCode.objects.filter(user=user).delete()  # Удаляем код после подтверждения
