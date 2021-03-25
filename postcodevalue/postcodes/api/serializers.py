from rest_framework import serializers
from postcodes.api.models import Outcode, NexusOutcode

class OutcodeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Outcode
        fields = ('outcode_code', 'listing_count', 'average_daily_rate')

class NexusSerializer(serializers.ModelSerializer):
  
    next_outcode_1 = OutcodeSerializer(read_only=True)
    next_outcode_2 = OutcodeSerializer(read_only=True)
    next_outcode_3 = OutcodeSerializer(read_only=True)
    next_outcode_4 = OutcodeSerializer(read_only=True)
    next_outcode_5 = OutcodeSerializer(read_only=True)
    next_outcode_6 = OutcodeSerializer(read_only=True)
    next_outcode_7 = OutcodeSerializer(read_only=True)
    next_outcode_8 = OutcodeSerializer(read_only=True)
    next_outcode_9 = OutcodeSerializer(read_only=True)
    next_outcode_10 = OutcodeSerializer(read_only=True)

    # next_outcode_1 = serializers.SlugRelatedField(slug_field='outcode_code', queryset=Outcode.objects.all(), required=False)
    # next_outcode_2 = serializers.SlugRelatedField(slug_field='outcode_code', queryset=Outcode.objects.all(), required=False)
    # next_outcode_3 = serializers.SlugRelatedField(slug_field='outcode_code', queryset=Outcode.objects.all(), required=False)
    # next_outcode_4 = serializers.SlugRelatedField(slug_field='outcode_code', queryset=Outcode.objects.all(), required=False)
    # next_outcode_5 = serializers.SlugRelatedField(slug_field='outcode_code', queryset=Outcode.objects.all(), required=False)
    # next_outcode_6 = serializers.SlugRelatedField(slug_field='outcode_code', queryset=Outcode.objects.all(), required=False)
    # next_outcode_7 = serializers.SlugRelatedField(slug_field='outcode_code', queryset=Outcode.objects.all(), required=False)
    # next_outcode_8 = serializers.SlugRelatedField(slug_field='outcode_code', queryset=Outcode.objects.all(), required=False)
    # next_outcode_9 = serializers.SlugRelatedField(slug_field='outcode_code', queryset=Outcode.objects.all(), required=False)
    # next_outcode_10 = serializers.SlugRelatedField(slug_field='outcode_code', queryset=Outcode.objects.all(), required=False)   
  

    class Meta:
        model = NexusOutcode
        fields = ('outcode_code', 'listing_count', 'average_daily_rate', 'distance_1', 'next_outcode_1',
                  'distance_2', 'next_outcode_2', 'distance_3', 'next_outcode_3', 'distance_4',
                 'next_outcode_4', 'distance_5', 'next_outcode_5', 'distance_6', 'next_outcode_6',
                  'distance_7','next_outcode_7','distance_8', 'next_outcode_8', 'distance_9',  
                 'next_outcode_9', 'distance_10', 'next_outcode_10')
  
  