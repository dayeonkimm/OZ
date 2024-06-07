from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path("", views.AddressList.as_view()),
    path("<int:address_id>/update", views.AddressDetail.as_view(), name="put_address"),
    path("<int:address_id>/delete", views.AddressDelete.as_view(), name="delete_address"),
    path("getToken", obtain_auth_token),

    path("login/simpleJWT", TokenObtainPairView.as_view()),
    path("login/simpleJWT/refresh", TokenRefreshView.as_view()),
    path("login/simpleJWT/verify", TokenVerifyView.as_view())
]
