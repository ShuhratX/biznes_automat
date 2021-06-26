from django.urls import path
from .views import LoanCreateView


urlpatterns = [

    path('create', LoanCreateView.as_view()),

]