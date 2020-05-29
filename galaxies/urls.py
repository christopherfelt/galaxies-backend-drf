from django.urls import path
from .views import GalaxiesList, GalaxyDetail, GetStarsByID

urlpatterns = [
    path('', GalaxiesList.as_view()),
    path('<int:pk>/', GalaxyDetail.as_view()),
    path('<int:pk>/stars/', GetStarsByID.as_view())
]
