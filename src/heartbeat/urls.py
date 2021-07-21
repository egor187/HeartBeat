from django.urls import path

from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("question", views.QuestionViewSet, basename="questions")

app_name = "heartbeat"

urlpatterns = [
    path("", views.RootAPIView.as_view(), name="root"),
    path("teams/", views.TeamListAPIView.as_view(), name="teams"),
    path("team/create/", views.TeamCreateAPIView.as_view(), name="create_team"),
    path("team/delete/<int:pk>/", views.TeamDeleteAPIView.as_view(), name="delete_team"),
    path("team/update/<int:pk>/", views.TeamUpdateAPIView.as_view(), name="update_team"),

    path("membership/", views.MembershipListAPIView.as_view(), name="memberships"),
    path("membership/create/", views.MembershipCreateAPIView.as_view(), name="create_membership"),
    path("membership/delete/<int:pk>/", views.MembershipDeleteAPIView.as_view(), name="delete_membership"),

] + router.urls
