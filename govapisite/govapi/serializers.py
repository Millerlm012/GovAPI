# serializers.py
from rest_framework import serializers

from .models import Governor

class GovernorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Governor
        fields = ('state',
                  'gov_Name',
                  'address',
                  'phone_Number',
                  'fax',
                  'media_Contact',
                  'state_Federal_Contact',
                  'gov_Website',
                  'gov_Bio',
                  'state_Website',
                  'coronavirues_Resources')
