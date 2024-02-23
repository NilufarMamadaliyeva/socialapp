from rest_framework import serializers
from .models import HitMusicModel


class HitMusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = HitMusicModel
        fields = "__all__"
