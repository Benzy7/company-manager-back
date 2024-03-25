from django.urls import path, include
from core.apis.company.view import CompanyViewSet, CompanyGenericViewSet
from core.apis.manager.view import ManagerViewSet
from core.apis.counter.view import CounterViewSet, CounterGenericViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('company', CompanyViewSet, basename='company')
router.register('manager', ManagerViewSet, basename='manager')
router.register('counter', CounterViewSet, basename='counter')

urlpatterns = [
    path('', include(router.urls)),
    path('companies/lite/', CompanyGenericViewSet.as_view({'get': 'get_companies_lite'}), name='company lite'),
    path('add-quotation/', CompanyGenericViewSet.as_view({'post': 'add_company_quotation'}), name='add company quotation'),
    path('add-points/', CounterGenericViewSet.as_view({'post': 'add_points'}), name='add points'),
]
