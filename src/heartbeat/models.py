from django.db import models

from src.profiles.models import CustomUser


class Team(models.Model):
    """
    Class to define Team
    """
    name = models.CharField(max_length=50, verbose_name="Name of the team")
    team_lead = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name="team leader",
        related_name="team_lead_teams"
    )
    members = models.ManyToManyField(
        CustomUser,
        through="Membership",
        verbose_name="team members",
        related_name="member_teams"
    )

    def __str__(self):
        return f"Team: {self.name}. Team_lead: {self.team_lead}. Members: {self.members.all()}"


class Membership(models.Model):
    """
    Class for extra data of membership to associate it with the relationship between two models
    """
    member = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="memberships")
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="membership")
    date_joined = models.DateField(verbose_name="date of joining")

    class Meta:
        unique_together = ["member", "team"]

    def __str__(self):
        return f"{self.member} joined team {self.team} at {self.date_joined}"


class Question(models.Model):
    text = models.TextField(verbose_name="text of the question")
    team_lead = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="questions")

    class Meta:
        unique_together = ["text", "team_lead"]


class HeartBeat(models.Model):
    question = models.ForeignKey(Question, on_delete=models.PROTECT, related_name="heartbeats")
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="heartbeats")
    member = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name="heartbeats")
    date_created = models.DateField(auto_now_add=True)
    yesterday_plan = models.TextField()
    today_plan = models.TextField()
