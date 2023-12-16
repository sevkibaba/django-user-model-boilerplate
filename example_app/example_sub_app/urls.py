from django.urls import path
from . import views

urlpatterns = [
    path('example-endpoint/', views.ExampleEndPoint.as_view()),

]
