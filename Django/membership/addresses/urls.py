from django.urls import path
from . import views

urlpatterns = [
    path("", views.Addresses.as_view()),
    path("<int:address_id>/update", views.AddressDetail.as_view(), name="put_address"),
    path("<int:address_id>/delete", views.AddressDelete.as_view(), name="delete_address")
]
