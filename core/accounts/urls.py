from django.urls import path , include
from .views import *
from django.contrib.auth.views import LogoutView

app_name='accounts'

urlpatterns = [
    path('login/' , CustomLoginView.as_view() , name='login'),
    path('logout/' , LogoutView.as_view(next_page='/accounts/login') , name='logout'),
    path("register/", RegisterPage.as_view(), name="register"),

    path('api/v1/' , include('accounts.api.v1.urls'))
]
