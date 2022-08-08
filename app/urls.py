from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('pc/',pc,name="pc"),
    path('pc/mechanics/',pc_mechanics,name="mechanics"),
    path('pc/waves/',pc_waves,name="waves"),
    path('pc/optics/',pc_optics,name="optics"),
    path('pc/nuclear/',pc_nuclear,name="nuclear"),
    path('pc/electricity/',pc_electricity,name="electricity"),
    path('pc/general/',pc_general,name="pcgeneral"),
    path('pc/matter/',pc_matter,name="matter"),

]