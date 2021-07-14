from rest_framework import serializers

from .models import Team


class TeamSerializer(serializers.ModelSerializer):
    team_lead = serializers.SlugRelatedField(
        slug_field="username",
        read_only=True
    )  # slugs "username" field instead "id"

    class Meta:
        model = Team
        fields = ["name", "team_lead", "members"]
