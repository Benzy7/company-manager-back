from rest_framework import serializers
from core.models import Counter



class CounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counter
        fields = '__all__'
