from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class ProtedtedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        response = {"status": "Request was permitted"}
        return Response(response)
