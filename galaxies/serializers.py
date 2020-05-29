from rest_framework import serializers
from .models import Galaxy
from stars.serializers import StarSerializer

class GalaxySerializer(serializers.ModelSerializer):

    class Meta:
        model = Galaxy
        fields = "__all__"
        depth = 1
