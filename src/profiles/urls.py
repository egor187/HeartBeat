from django.urls import path

from . import views

app_name = "profiles"

urlpatterns = [
    path("", views.ProfileListView.as_view(), name="profiles"),
    path("<int:pk>/", views.ProfileDetailView.as_view(), name="profile_detail"),
]
