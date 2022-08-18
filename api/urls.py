
from django.urls import path
from rest_framework.authtoken import views as authtoken_views
from authentication.views import UserEndpoint


urlpatterns = [
    path('auth/users', UserEndpoint.as_view()),
    path('token/', authtoken_views.obtain_auth_token),
]