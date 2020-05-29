from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

from .models import Star
from .serializers import StarSerializer

class StarsList(APIView):
    def get(self, resquest, format=None):
        stars = Star.objects.all()
        serializer = StarSerializer(stars, many=True)
        return Response(serializer.data)


class StarDetail(APIView):
    def get_object(self, pk):
        try:
            star = Star.objects.get(pk=pk)
            return star
        except star.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        star = self.get_object(pk=pk)
        serializer = StarSerializer(star)
        return Response(serializer.data)

