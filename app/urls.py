from django.urls import path
from .views import home, pc, pc_mechanics

urlpatterns = [
    path('',home,name="home"),
    path('pc/',pc,name="pc"),
    path('pc/mechanics/',pc_mechanics,name="mechanics"),

]