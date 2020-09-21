from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    """ User serializer for user model """
    password = serializers.CharField(write_only=True)
    class Meta:
        model = get_user_model()
        fields = (
            'id', 'username', 'password',
            'first_name', 'last_name',
        )
        read_only_fields = ('id',)

class LogInSerializer(TokenObtainPairSerializer):
    """ custom claim for tokens """
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        user_data = UserSerializer(user).data
        for key, value in user_data.items():
            if key != 'id':
                token[key] = value
        return token
