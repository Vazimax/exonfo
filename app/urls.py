from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name="home"),
    # PC:
    path('pc/',pc,name="pc"),
    path('pc/mechanics/',pc_mechanics,name="mechanics"),
    path('pc/waves/',pc_waves,name="waves"),
    path('pc/optics/',pc_optics,name="optics"),
    path('pc/nuclear/',pc_nuclear,name="nuclear"),
    path('pc/electricity/',pc_electricity,name="electricity"),
    path('pc/general/',pc_general,name="pcgeneral"),
    path('pc/matter/',pc_matter,name="matter"),
    path('pc/organic/',pc_organic,name="organic-chemistry"),
    path('pc/chemical-reactions/',pc_reactions,name="chemical-reactions"),
    path('pc/measurement/',pc_measurement,name="measurement-chemistry"),
    # SVT:
    path('svt/',svt,name="svt"),
    path('svt/general/',svt_general,name="svtgeneral"),
    path('svt/ecology/',svt_ecology,name="ecology"),
    path('svt/rep_plant/',svt_rep_plant,name="rep_plant"),
    path('svt/geology/',svt_geology,name="geology"),
    path('svt/genetics/',svt_genetics,name="genetics"),
    path('svt/organic/',svt_organic,name="svt_organic"),
    path('svt/nerves/',svt_nerves,name="nerves"),
    path('svt/immunology/',svt_immunity,name="immunity"),
    path('svt/rep_human/',svt_rep_human,name="rep_human"),
    # MATH:
    path('math/',math,name="math"),
    path('math/general/',math_general,name="mathgeneral"),
    path('math/geometry/',math_geometry,name="geometry"),
    path('math/setca/',math_setca,name="mathsetca"),
]