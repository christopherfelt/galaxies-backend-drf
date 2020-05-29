from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import Http404

from .models import Galaxy
from .serializers import GalaxySerializer
from stars.serializers import StarSerializer
from stars.models import Star


class GalaxiesList(APIView):
    def get(self, request, format=None):
        galaxies = Galaxy.objects.all()
        serializer = GalaxySerializer(galaxies, many=True)
        return Response(serializer.data)



class GalaxyDetail(APIView):
    def get_object(self, pk):
        try:
            galaxy = Galaxy.objects.get(pk=pk)
            return galaxy
        except galaxy.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        galaxy = self.get_object(pk=pk)
        serializer = GalaxySerializer(galaxy)
        return Response(serializer.data)

class GetStarsByID(APIView):
    def get(self, request, pk, format=None):
        stars = Star.objects.filter(galaxy_id=pk)
        serializer = StarSerializer(stars, many=True)
        return Response(serializer.data)