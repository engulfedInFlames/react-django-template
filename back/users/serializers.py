from django.db import transaction
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "pk",
            "email",
            "nickname",
            "created_at",
            "updated_at",
        )

    def create(self, validated_data):
        return super().create(validated_data)


class UserPrivateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "pk",
            "email",
            "email_verified",
            "nickname",
            "is_active",
            "created_at",
            "updated_at",
        )


class UserSimpleSerializer(serializers.ModelSerializer):
    ...
