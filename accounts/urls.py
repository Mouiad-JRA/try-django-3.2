from django.urls import path, include

from accounts.views import login_view, logout_view, register_view

urlpatterns = [
    path('login/', login_view, name="user-login"),
    path('logout/', logout_view, name="user-logout"),
    path('register/', register_view, name="user-register"),
]