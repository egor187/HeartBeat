from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    _is_team_lead = models.BooleanField(default=False)

    @property
    def is_team_lead(self):
        return self._is_team_lead

    @is_team_lead.setter
    def is_team_lead(self, value: bool) -> None:
        self._is_team_lead = value
