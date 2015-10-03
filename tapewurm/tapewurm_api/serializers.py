from rest_framework import serializers
from tapewurm.tapewurm_api.models import Mix, Track

class MixSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mix
        fields = ('url_identifier', 'date_submitted', 'name', 'image_url')


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('musicbrainz_id', 'mix', 'order', 'note')
