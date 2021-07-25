from decimal import Decimal

from django.db.models import Sum

from .models import HeartBeat, Team


class HeartBeatEntry:
    def __init__(self, team: Team, count: Decimal):
        self.team = team
        self.count = count


def get_team_beats():
    data = []

    queryset = HeartBeat.objects.values("team").annotate(
        count=Sum("id")
    )

    for entry in queryset:
        heart_beat_entry = HeartBeatEntry(entry["team"], entry["count"])
        data.append(heart_beat_entry)

    return data
