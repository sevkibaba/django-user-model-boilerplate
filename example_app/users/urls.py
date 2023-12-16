from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path('', views.UserList.as_view()),
    path('sign-up/', views.SignUpView.as_view()),
    path('sign-in/', obtain_auth_token),
    path('sign-out/', views.SignOutView.as_view()),
    path('details/', views.UserDetails.as_view()),
    path('change-password/', views.ChangePasswordView.as_view()),
]
