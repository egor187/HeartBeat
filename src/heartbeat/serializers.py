from rest_framework import serializers

from .models import Team, Membership
from ..profiles.models import CustomUser


class MembershipSerializer(serializers.ModelSerializer):
    date_joined = serializers.DateTimeField(read_only=True)
    username = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    email = serializers.SlugField()

    class Meta:
        model = Membership
        fields = ["id", "date_joined", "username", "email"]


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "email"]


class TeamSerializer(serializers.ModelSerializer):
    # slugs "username" field instead "id"
    # team_lead = serializers.SlugRelatedField(
    #     slug_field="username",
    #     read_only=True
    # )

    #  Nested serializer realization
    team_lead = CustomUserSerializer(read_only=True)
    members = MembershipSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ["id", "name", "team_lead", "members"]
