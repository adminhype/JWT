from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.urls import path

from .views import RegistrationView, MoinWorldView


urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('moin/', MoinWorldView.as_view(), name='moin'),
]
