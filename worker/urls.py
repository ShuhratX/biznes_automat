from django.urls import path
from .views import WorkerCreateView


urlpatterns = [

    path('create', WorkerCreateView.as_view()),

]