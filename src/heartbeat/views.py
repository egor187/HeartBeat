from django.db.utils import IntegrityError

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Team, Membership, Question, HeartBeat
from .serializers import TeamSerializer, MembershipReadSerializer, MembershipWriteSerializer, QuestionWriteSerializer, \
    QuestionReadSerializer, HeartBeatReadSerializer, HeartBeatWriteSerializer
from .custom_permissions import IsQuestionOwner, IsTeamLead


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

    # Realization below (without using validation on 'serializer' level) with hardcoded returning Response
    # with 403-status and row error message. More convenient realization is to set field validation on serializater
    # level with raising serializers.ValidationError

    # def create(self, request, *args, **kwargs):
    #     """
    #     Override parent method to allow only to 'is_team_lead' users to create team
    #     """
    #     if self.request.user.is_team_lead:
    #         serializer = self.get_serializer(data=request.data)
    #         serializer.is_valid(raise_exception=True)
    #         self.perform_create(serializer)
    #         headers = self.get_success_headers(serializer.data)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    #     else:
    #         return Response(data={"msg": "current user isn't teamlead"}, status=status.HTTP_403_FORBIDDEN)


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
    serializer_class = MembershipReadSerializer


class MembershipCreateAPIView(generics.CreateAPIView):
    queryset = Membership.objects.all()
    serializer_class = MembershipWriteSerializer


class MembershipDeleteAPIView(generics.DestroyAPIView):
    queryset = Membership.objects.all()
    serializer_class = MembershipReadSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    permission_classes = [IsQuestionOwner, ]

    def get_serializer_class(self):
        if self.action in ("create", "update", "destroy"):
            return QuestionWriteSerializer
        else:
            return QuestionReadSerializer

    # unique_constrain validation and auto populating current user to related field "team-lead" provided
    # by HiddenField and UniqueTogetherValidator on serializer class.
    # The implementation below is less convenient and less intuitive

    # def perform_create(self, serializer):
    #     serializer.save(team_lead=self.request.user)
    #
    # def create(self, request, *args, **kwargs):
    #     """
    #     override to handle Question-model unique_together constraint
    #     """
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #
    #     try:
    #         self.perform_create(serializer)
    #     except IntegrityError:
    #         return Response(data={"message": "unique constraint violation"}, status=status.HTTP_409_CONFLICT)
    #     else:
    #         headers = self.get_success_headers(serializer.data)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    #
    # def update(self, request, *args, **kwargs):
    #     """
    #     override to handle Question-model unique_together constraint
    #     """
    #     partial = kwargs.pop('partial', False)
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #     serializer.is_valid(raise_exception=True)
    #
    #     try:
    #         self.perform_update(serializer)
    #         if getattr(instance, '_prefetched_objects_cache', None):
    #             # If 'prefetch_related' has been applied to a queryset, we need to
    #             # forcibly invalidate the prefetch cache on the instance.
    #             instance._prefetched_objects_cache = {}
    #     except IntegrityError:
    #         return Response(data={"message": "unique constraint violation"}, status=status.HTTP_409_CONFLICT)
    #     else:
    #         return Response(serializer.data)


class HeartBeatViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        """
        return queryset only for related teams in which current user is team_lead
        """
        if self.request.user.is_team_lead:
            return HeartBeat.objects.filter(team__team_lead=self.request.user)
        else:
            return HeartBeat.objects.filter(creator=self.request.user)

    def get_serializer_class(self):
        if self.action in ("create", "update", "destroy"):
            return HeartBeatWriteSerializer
        else:
            return HeartBeatReadSerializer
