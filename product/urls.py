from django.urls import path
from .views import *


urlpatterns = [
    path('create', ProductCreateView.as_view()),
    path('partner-create', PartnerCreateView.as_view()),
    path('sale-create', SaleCreateView.as_view()),
    path('worker-create', WorkerCreateView.as_view()),
    path('loan-create', LoanCreateView.as_view()),
    path('expense-create', ExpenseCreateView.as_view()),

]
