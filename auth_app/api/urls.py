from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from django.urls import path

from .views import CookieTokenRefreshView, CustomTokenObtainPairView, RegistrationView, MoinWorldView


urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CookieTokenRefreshView.as_view(), name='token_refresh'),

    path('moin/', MoinWorldView.as_view(), name='moin'),
]
