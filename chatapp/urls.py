from django.urls import path
from .views import RegisterView, LoginView, ChatView, TokenBalanceView, index
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('chat/', ChatView.as_view(), name='chat'),
    path('token-balance/', TokenBalanceView.as_view(), name='token-balance'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('index/', index, name='index'),
]
