from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("", views.AddressList.as_view()),
    path("<int:address_id>/update", views.AddressDetail.as_view(), name="put_address"),
    path("<int:address_id>/delete", views.AddressDelete.as_view(), name="delete_address"),
    path("getToken", obtain_auth_token)

]
