from django.urls import path
from .views import PartnerCreateView


urlpatterns = [

    path('create', PartnerCreateView.as_view()),

]