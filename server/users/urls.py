from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from . import views


app_name = 'users'

urlpatterns = [
    path(
        route='sign_up/',
        view=views.SignUpView.as_view(),
        name='sign_up'),
    path(
        route='log_in/',
        view=views.LogInView.as_view(),
        name='log_in'),
    path(
        route='token/refresh/',
        view=TokenRefreshView.as_view(),
        name='token_refresh'),
]