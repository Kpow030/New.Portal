from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('accounts/login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
]
