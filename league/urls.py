"""dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.default_view),
    path('matches/<str:season_name>/', views.display_all_matches),
    path('matches/<str:season_name>/<int:match_id>/', views.display_match_details, name='match_details'),
    path('matches/team/<str:team>/<str:location>', views.display_matches_team, name='matches_team'),
    path('matches/team/<str:team>/<str:result>/<str:location>', views.display_matches_team_result),
    path('matches/<str:team1>_<str:team2>', views.display_matches_bw_teams),
    path('matches/comebacks/<str:season_name>/<str:team>/<str:location>', views.comebacks),
]
