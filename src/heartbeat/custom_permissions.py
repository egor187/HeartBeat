from rest_framework import permissions


class IsQuestionOwner(permissions.BasePermission):
    """
    access to manipulate with 'Question' instance only for question creator
    """
    def has_object_permission(self, request, view, obj):
        return request.user == obj.team_lead


class IsTeamLead(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_team_lead
