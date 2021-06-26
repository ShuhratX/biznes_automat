from django.urls import path
from .views import ProductCreateView


urlpatterns = [
    path('create', ProductCreateView.as_view()),

]
