from django.urls import path
from .views import InvoiceDetailsListCreate, InvoiceDetailsRetrieveUpdateDelete, UnitListCreate, UnitRetrieveUpdateDelete


urlpatterns = [

    path('invoice-details', InvoiceDetailsListCreate.as_view()),
    path('invoice-details/<int:pk>/', InvoiceDetailsRetrieveUpdateDelete.as_view()),
    path('unit-list', UnitListCreate.as_view()),
    path('unit-list/<int:pk>/', UnitRetrieveUpdateDelete.as_view()),



]
