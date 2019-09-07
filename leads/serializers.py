from rest_framework import serializers
from leads.models import Lead

# Lead Serializer
class LeadSerializer(serializers.ModelSerializer):
  # turning our Lead model into serializer
  class Meta:
    model = Lead
    fields = '__all__'

  
