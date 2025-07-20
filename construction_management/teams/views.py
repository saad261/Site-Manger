from django.shortcuts import render
from .forms import SiteForm
from .forms import LocationForm
from .forms import TaskForm
from .forms import TeamForm
from .models import Team
from .models import Task
from .models import Location
from django.http import HttpResponseRedirect

# Create your views here.

def add_sites(reguset):
    submitted = False
    if reguset.method == "POST":
        form = SiteForm(reguset.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/add_sites?submitted=True")
    else:
        form = SiteForm
        if "submitted" in reguset.GET:
            submitted = True

    return render(reguset, "teams/add_sites.html", {"form": form, "submitted": submitted})


def add_teams(reguset):
    submitted = False
    if reguset.method == "POST":
        form = TeamForm(reguset.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/add_teams?submitted=True")
    else:
        form = TeamForm
        if "submitted" in reguset.GET:
            submitted = True

    return render(reguset, "teams/add_teams.html", {"form": form, "submitted": submitted})

def add_tasks(reguset):
    submitted = False
    if reguset.method == "POST":
        form = TaskForm(reguset.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/add_tasks?submitted=True")
    else:
        form = TaskForm
        if "submitted" in reguset.GET:
            submitted = True

    return render(reguset, "teams/add_tasks.html", {"form": form, "submitted": submitted})

def add_locations(reguset):
    submitted = False
    if reguset.method == "POST":
        form = LocationForm(reguset.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/add_locations?submitted=True")
    else:
        form = LocationForm
        if "submitted" in reguset.GET:
            submitted = True

    return render(reguset, "teams/add_locations.html", {"form": form, "submitted": submitted})

def home(reguset):
    name = "saad"
    return render(reguset,
        "teams/home.html",{
        "name":name
                  })


def all_teams(reguset):
    team_list = Team.objects.all()
    return render(reguset, "teams/team_lists.html",
                  {"team_list": team_list})

def manager_login(reguset):
    return render(reguset, "teams/manager_login.html", {})

def team_login(reguset):
    return render(reguset, "teams/team_login.html", {})

