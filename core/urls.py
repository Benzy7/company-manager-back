from django.urls import path, include
from core.apis.company.view import CompanyViewSet
from core.apis.manager.view import ManagerViewSet
from core.apis.counter.view import CounterViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('company', CompanyViewSet, basename='company')
router.register('manager', ManagerViewSet, basename='manager')
router.register('counter', CounterViewSet, basename='counter')

urlpatterns = [
    path('', include(router.urls)),
    # path('check-email/', EmailCheck.as_view() , name='check_email'),
]
