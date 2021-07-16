from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Team
from .serializers import TeamSerializer


class RootAPIView(APIView):
    def get(self, request):
        return Response(
            {
                "teams": reverse("heartbeat:teams", request=request)
            }
        )


class TeamListAPIView(generics.ListAPIView):
    """
    View for listing a Team queryset.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def get_queryset(self):
        """
        Return only those teams in which 'request.user' is team_lead
        """
        queryset = Team.objects.filter(team_lead=self.request.user)
        return queryset


class TeamCreateAPIView(generics.CreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def perform_create(self, serializer):
        """
        save instance with 'request.user' on 'team_lead' field
        """
        serializer.save(team_lead=self.request.user)


class TeamDeleteAPIView(generics.DestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def delete(self, request, *args, **kwargs):
        """
        Override for restrict access to delete teams only by team_lead who created that team
        """
        instance = self.get_object()
        if instance.team_lead == self.request.user:
            return super().destroy(request, args, kwargs)
        else:
            return Response(status=404)