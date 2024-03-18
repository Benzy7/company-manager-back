from genericpath import exists
from rest_framework import viewsets, permissions
from authentication.models import CustomUser
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

class EmailCheck(APIView):
    """
    Check if Email exists in users.
    
    * Dosent Require authentication.
    """
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        try:            
            email = request.data.get('email')
            if CustomUser.objects.filter(email=email).exists():
                return Response(data={"info": "EMAIL_FOUND", "exists": True}, status=status.HTTP_200_OK)
            return Response(data={"info": "EMAIL_NOT_FOUND", "exists": False}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={"info": "ERROR", "message": e}, status=status.HTTP_400_BAD_REQUEST)
