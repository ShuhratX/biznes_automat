from django.urls import path
from .views import ExpenseCreateView


urlpatterns = [
    path('create', ExpenseCreateView.as_view()),
]