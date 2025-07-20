from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('teams', views.all_teams, name="list-teams"),
    path('add_sites', views.add_sites, name="add_sites"),
    path('add_locations', views.add_locations, name="add_locations"),
    path('add_tasks', views.add_tasks, name="add_tasks"),
    path('add_teams', views.add_teams, name="add_teams"),
    path('manager_login', views.manager_login, name="manager_login"),
    path('team_login', views.team_login, name="team_login"),

    ]