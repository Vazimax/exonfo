from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('pc/',pc,name="pc"),
    path('pc/mechanics/',pc_mechanics,name="mechanics"),
    path('pc/electricity/',pc_electricity,name="electricity"),
]