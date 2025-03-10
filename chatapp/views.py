from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password
from django.db import transaction
from .models import User, Chat
from .serializers import UserSerializer, ChatSerializer
from django.shortcuts import render

# User Registration API
class RegisterView(APIView):
    authentication_classes = []  # Allow unauthenticated access
    permission_classes = []      # No restrictions on registration

    def post(self, request):
        with transaction.atomic():
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                user = serializer.save()  # Save the user instance
                
                # Set and hash the password properly
                user.set_password(serializer.validated_data['password'])
                user.save()  # Save again after hashing password ✅

                # Generate JWT tokens
                refresh = RefreshToken.for_user(user)
                return Response({
                    'message': 'Registration successful!',
                    'access': str(refresh.access_token),
                    'refresh': str(refresh)
                }, status=status.HTTP_201_CREATED)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# User Login API
class LoginView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        username = request.data.get("username", "").strip()  # Removed `.lower()`
        password = request.data.get("password", "").strip()

        try:
            user = User.objects.get(username=username)
            if user.check_password(password):  # ✅ Correct password check
                refresh = RefreshToken.for_user(user)
                return Response({
                    "message": "Login successful!",
                    "access": str(refresh.access_token),
                    "refresh": str(refresh)
                }, status=status.HTTP_200_OK)
            return Response({"error": "Invalid username or password"}, status=status.HTTP_401_UNAUTHORIZED)
        except User.DoesNotExist:
            return Response({"error": "Invalid username or password"}, status=status.HTTP_401_UNAUTHORIZED)


# Chat API
class ChatView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        message = request.data.get('message', '').strip()

        if not message:
            return Response({'error': 'Message cannot be empty'}, status=status.HTTP_400_BAD_REQUEST)

        if not hasattr(user, 'tokens') or user.tokens < 100:  # Ensure tokens field exists
            return Response({'error': 'Insufficient tokens'}, status=status.HTTP_402_PAYMENT_REQUIRED)

        with transaction.atomic():
            response = f"AI Response to '{message}'"
            Chat.objects.create(user=user, message=message, response=response)
            user.tokens -= 100
            user.save()

        return Response({
            'message': message,
            'response': response,
            'remaining_tokens': user.tokens
        }, status=status.HTTP_200_OK)

# Token Balance API
class TokenBalanceView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print(f"Authenticated user: {request.user}")  # Debugging
        if request.user.is_anonymous:
            return Response({"detail": "User not found", "code": "user_not_found"}, status=404)

        return Response({
            'user_id': request.user.id,
            'username': request.user.username,
            'tokens': request.user.tokens  # ✅ Use request.user instead of user
        }, status=status.HTTP_200_OK)



def index(request):
    return render(request, 'chatapp/index.html')
