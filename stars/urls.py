from django.urls import path
from .views import StarsList, StarDetail

urlpatterns = [
    path('', StarsList.as_view()),
    path('<int:pk>/', StarDetail.as_view())
]
