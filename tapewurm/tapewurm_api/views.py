from datetime import datetime
import uuid
import json
from django.shortcuts import render
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response

from tapewurm.tapewurm_api.models import Mix, Track
from tapewurm.tapewurm_api.serializers import MixSerializer, TrackSerializer

#TODO: Verify requests to stop 500s
class MixView(APIView):
    def get(self, request):
        mix_url_id = request.query_params['mix_id']

        try:
            mix = Mix.objects.get(url_identifier=mix_url_id)
        except Mix.DoesNotExist:
            raise Http404("Mix does not exist")

        mix_data =  MixSerializer(mix).data
        tracks_data = TrackSerializer(Track.objects.get(mix=mix)).data
        return Response({'mix': mix_data, 'tracks': tracks_data})

    def post(self, request):
        data = json.loads(request.body)
        print data

        mix = Mix()
        mix.name = data['name']
        mix.picture_url = data['image_url']
        print datetime.now()
        mix.date_submitted = datetime.now()
        mix.url_identifier = uuid.uuid4().hex[:8]
        mix.save()

        for track in data['tracks']:
            track_object = Track()
            track_object.note = track['note']
            track_object.mix = mix
            track_object.order = track['order']
            track_object.musicbrainz_id = 'abc'#track['musicbrainz_id']
            track_object.save()

        return Response({'url': mix.url_identifier})
