from logging import Manager
from rest_framework import viewsets, permissions
from core.models import Company, Manager, Quotation
from core.pagination import CustomPagination
from .serializers import CompanySerializer, CompanyDetailSerializer
from core.apis.manager.serializers import ManagerSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from django.db import transaction



class CompanyViewSet(viewsets.ModelViewSet):
	queryset = Company.objects.all()
	permission_classes = [permissions.IsAuthenticated]
	pagination_class = CustomPagination
	filter_backends = [DjangoFilterBackend, filters.SearchFilter]
	filterset_fields =  ['name', 'reason', 'siret', 'postal_code']
	search_fields = ['name', 'reason', 'siret', 'postal_code']

	def get_serializer_class(self):
		if self.action == 'retrieve':
			return CompanyDetailSerializer
		else:
			return CompanySerializer

class CompanyGenericViewSet(GenericViewSet):
	permission_classes = [permissions.IsAuthenticated]

	def get_companies_lite(self, request):
		siret_filter = request.GET.get('siret')
		queryset = Company.objects.filter(siret__contains=siret_filter).values('id', 'name', 'siret', 'reason', 'postal_code')
		return Response(queryset)

	@transaction.atomic
	def add_company_quotation(self, request):
		try:
			data = request.data
   
			company = None
			company_data = data.get('company')
			if company_data['id'] not in ("", None):
				company = Company.objects.get(pk=company_data['id'])
			company_serializer = CompanySerializer(company, data=company_data)
			if company_serializer.is_valid():
				company_instance = company_serializer.save()
			else:
				return Response(data={"info": "INVALID_COMPANY_DATA" }, status=status.HTTP_200_OK)

			manager = None
			manager_data = data.get('manager')
			manager_data['company'] = company_instance.id
			if manager_data['id'] not in ("", None):
				manager = Manager.objects.get(pk=manager_data['id'])
			manager_serializer = ManagerSerializer(manager , data=manager_data)
			if manager_serializer.is_valid():
				manager_instance = manager_serializer.save()
			else:
				print(manager_serializer.errors)
				return Response(data={"info": "INVALID_MANAGER_DATA"}, status=status.HTTP_200_OK)

			Quotation.objects.create(
				company_name=company_data['name'],
				company_reason=company_data['reason'],
				company_siret=company_data['siret'],
				company_postal_code=company_data['postal_code'],
				manager_first_name=manager_data['first_name'],
				manager_last_name=manager_data['last_name'],
				manager_phone_number=manager_data['phone_number'],
				manager_email=manager_data['email'],
				company=company_instance,
				manager=manager_instance
			)
			return Response(data={"info": 'SUCCESS', "company": CompanySerializer(company_instance).data}, status=status.HTTP_200_OK)

		except Company.DoesNotExist as e:
			transaction.set_rollback(True)
			return Response(data={"info": 'COMPANY_NOT_FOUND', "detail":'company not found'}, status=status.HTTP_404_NOT_FOUND)
		except Manager.DoesNotExist as e:
			transaction.set_rollback(True)
			return Response(data={"info": 'MANAGER_NOT_FOUND', "detail":'manager not found'}, status=status.HTTP_404_NOT_FOUND)
		except Exception as e:
			transaction.set_rollback(True)
			return Response(data={"info": 'ERROR', "detail":str(e)}, status=status.HTTP_400_BAD_REQUEST)
