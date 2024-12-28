from django.urls import path

from accounts.views import UserRegistrationView, UserLoginView, UserProfileView, UserChangePasswordView, \
    UserSendPasswordResetLinkView, UserPasswordResetView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('change-password/', UserChangePasswordView.as_view(), name='change_password'),
    path('send-password-reset-email/', UserSendPasswordResetLinkView.as_view(), name='send_password_reset_email'),
    path('reset-password/<uid>/<token>', UserPasswordResetView.as_view(), name='reset_password'),
]