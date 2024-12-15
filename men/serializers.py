from rest_framework import serializers

from .models import Men


class MenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Men
        fields = ('title', 'cat_id')
        