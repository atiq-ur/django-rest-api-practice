from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.serializers import UserRegistrationSerializer, UserLoginSerializer, UserProfileSerializer, \
    UserChangePasswordSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.renderers import JSONRenderer


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class UserRegistrationView(APIView):
    renderer_classes = [JSONRenderer]

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = get_tokens_for_user(user)
        return Response(
            {
                'token': str(token),
                'user': serializer.data,
                'message': 'User registered successfully',
            },
            status=status.HTTP_201_CREATED
        )


class UserLoginView(APIView):
    renderer_classes = [JSONRenderer]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get('email')
        password = serializer.data.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            token = get_tokens_for_user(user)
            return Response(
                {
                    'token': str(token),
                    'user': serializer.data,
                    'message': 'User logged in successfully',
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {
                    'errors': {'non_field_errors': ['Email or Password is not Valid']}
                }
                , status=status.HTTP_400_BAD_REQUEST
            )


class UserProfileView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


class UserChangePasswordView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = UserChangePasswordSerializer(data=request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        return Response(
            {
                'message': 'Password Changed Successfully'
            },
            status=status.HTTP_200_OK
        )
