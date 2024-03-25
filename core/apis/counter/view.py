from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import CounterSerializer
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import viewsets, permissions
from core.models import Counter
from django.db import transaction



class CounterViewSet(viewsets.ViewSet):
	permission_classes = [permissions.IsAuthenticated]

	def create(self, request):
		serializer = CounterSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CounterGenericViewSet(GenericViewSet):
	permission_classes = [permissions.IsAuthenticated]

	@transaction.atomic
	def add_points(self, request):
		try:
			data = request.data
			print(data)
   
			serializer = CounterSerializer(data=data, many=True)
			serializer.is_valid(raise_exception=True)

			counters = Counter.objects.bulk_create([Counter(**item) for item in serializer.validated_data])
			return Response(data={"info": 'SUCCESS', "counters_created": len(counters)}, status=status.HTTP_201_CREATED)
		except Exception as e:
			transaction.set_rollback(True)
			return Response(data={"info": 'ERROR', "detail":str(e)}, status=status.HTTP_400_BAD_REQUEST)
