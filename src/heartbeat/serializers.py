from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Team, Membership, Question, HeartBeat
from ..profiles.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "email"]


class MembershipReadSerializer(serializers.ModelSerializer):
    member = CustomUserSerializer()

    class Meta:
        model = Membership
        fields = ["team", "date_joined", "member"]


class MembershipWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = ["member", "date_joined", "team"]


class TeamSerializer(serializers.ModelSerializer):
    # slugs "username" field instead "id"
    # team_lead = serializers.SlugRelatedField(
    #     slug_field="username",
    #     read_only=True
    # )

    #  Nested serializer realization
    team_lead = CustomUserSerializer(read_only=True)
    members = CustomUserSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ["id", "name", "team_lead", "members"]


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ["id", "text", "team_lead"]
        read_only_fields = ["id", "team_lead"]
        # validators = [
        #     UniqueTogetherValidator(
        #         queryset=Question.objects.all(),
        #         fields=("text", "team_lead"),
        #         message="Such question already created by current user"
        #     )
        # ]
