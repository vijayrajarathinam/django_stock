from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, CharField


class UserSerializer(ModelSerializer):
    password = CharField(write_only=True, style={"input_type": "password"})

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def create(self, validated_data):

        user = User.objects.create_user(
            validated_data["username"],
            validated_data["email"],
            validated_data["password"],
        )

        return user
