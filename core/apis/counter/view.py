from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import CounterSerializer

class CounterViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = CounterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
