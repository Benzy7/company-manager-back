from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UsersTokenObtainPairSerializer

class UsersTokenObtainPairView(TokenObtainPairView):
    serializer_class = UsersTokenObtainPairSerializer
