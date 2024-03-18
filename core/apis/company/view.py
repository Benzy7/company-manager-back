from rest_framework import viewsets, permissions
from core.models import Company
from core.pagination import CustomPagination
from .serializers import CompanySerializer, CompanyDetailSerializer



class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPagination

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CompanyDetailSerializer
        else:
            return CompanySerializer
