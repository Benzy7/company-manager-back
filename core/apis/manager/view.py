from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import ManagerSerializer

class ManagerViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = ManagerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
