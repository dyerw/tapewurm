import datetime
import uuid
import json
from django.shortcuts import render
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView

from tapewurm.tapewurm_api.models import Mix, Track
from tapewurm.tapewurm_api.serializers import MixSerializer, TrackSerializer

#TODO: Verify requests to stop 500s
class MixView(APIView):
    def get(self, request):
        mix_url_id = request.query_params['mix_id']

        try:
            mix_data = MixSerializer(Mix.objects.get(url_identifier=mix_url_id)).data
        except Mix.DoesNotExist:
            raise Http404("Mix does not exist")

        tracks_data = TrackSerializer(Track.objects.get(mix=mix_data.pk)).data
        return Response({'mix': mix_data, 'tracks': tracks_data})

    def post(self, request):
        print json.loads(request.body)
        return Response()

        mix = Mix.objects.create()
        mix.name = request['name']
        mix.picture_url = request['picture_url']
        mix.date_submitted = datetime.datetime.now()
        mix.url_identifier = uuid.uuid().hex[:8]
        mix.save()

        for track in request['tracks']:
            track_object = Track.objects.create()
            track_object.note = track['note']
            track_object.mix = mix.pk
            track_object.order = track['order']
            track_object.musicbrainz_id = track['musicbrainz_id']
            track.save()
