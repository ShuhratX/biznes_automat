from django.urls import path
from .views import SaleCreateView


urlpatterns = [

    path('create', SaleCreateView.as_view()),

]