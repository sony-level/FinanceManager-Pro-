from django.urls import path

from . import views

app_name = "companies"

urlpatterns = [
    path("", views.company_list, name="list"),
    path("create", views.company_create, name="create"),
    path("<uuid:company_id>", views.company_detail, name="detail"),
]

# URLs pour les tenants (multi-tenant)
tenants_urlpatterns = [
    path("", views.tenant_list, name="tenant-list"),
    path("switch", views.tenant_switch, name="tenant-switch"),
    path("current", views.tenant_current, name="tenant-current"),
    # Gestion de l'équipe
    path("members/", views.team_members_list, name="team-members-list"),
    path("members/invite", views.team_member_invite, name="team-member-invite"),
    path(
        "members/<uuid:membership_id>",
        views.team_member_remove,
        name="team-member-remove",
    ),
    path(
        "members/<uuid:membership_id>/role",
        views.team_member_update,
        name="team-member-update",
    ),
]
