from django.urls import path
from .views import SaleCreateView, PurchaseCreateView


urlpatterns = [

    path('sale-create', SaleCreateView.as_view()),
    path('purchase-create', PurchaseCreateView.as_view()),

]