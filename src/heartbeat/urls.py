from django.urls import path

from . import views

app_name = "heartbeat"

urlpatterns = [
    path("", views.RootAPIView.as_view(), name="root"),
    path("teams/", views.TeamListAPIView.as_view(), name="teams"),
    path("team/create/", views.TeamCreateAPIView.as_view(), name="create_team"),
    path("team/delete/<int:pk>/", views.TeamDeleteAPIView.as_view(), name="delete_team"),
]
