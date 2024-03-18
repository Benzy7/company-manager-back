from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import AuthenticationFailed


class UsersTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'email'

    def validate(self, attrs):
        try :
            print("attrs", attrs)
            data = super().validate(attrs)
            return data
        except AuthenticationFailed as e:
            print("AuthenticationFailed", e)
            raise AuthenticationFailed({"Info": "CREDENTIALS_NOT_VALID"})