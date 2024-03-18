from rest_framework_simplejwt.views import TokenRefreshView
from authentication.apis.token.view import UsersTokenObtainPairView
from django.urls import path, include
from rest_framework import routers
from authentication.apis.user.view import UserViewSet, EmailCheck

router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', UsersTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('check-email/', EmailCheck.as_view() , name='check_email'),
]