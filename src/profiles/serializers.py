from rest_framework import serializers

from src.profiles.models import CustomUser


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ["id", "username", "team_lead_teams"]
