from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Team, Membership
from .serializers import TeamSerializer, MembershipSerializer


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
        Override parent method to perform create team instance with predefined 'team_lead' field with self.request
        """
        serializer.save(team_lead=self.request.user)

    def create(self, request, *args, **kwargs):
        """
        Override parent method to allow only to 'is_team_lead' users to create team
        """
        if self.request.user.is_team_lead:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class TeamDeleteAPIView(generics.DestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def delete(self, request, *args, **kwargs):
        """
        Override for restrict access to delete teams only by team_lead who created that team and
        additional check for self.request.user is team_lead
        """
        instance = self.get_object()
        if instance.team_lead == self.request.user and self.request.user.is_team_lead:
            return super().destroy(request, args, kwargs)
        else:
            return Response(status=404)


class TeamUpdateAPIView(generics.UpdateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class MembershipListAPIView(generics.ListAPIView):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer


class MembershipCreateAPIView(generics.CreateAPIView):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer


class MembershipDeleteAPIView(generics.DestroyAPIView):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer
