from rest_framework import serializers
from core.models import Counter



class CounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counter
        fields = '__all__'
        
    def validate(self, data):
        validated_data = super().validate(data)

        pdl = validated_data.get('pdl')
        pdl_type = validated_data.get('pdl_type')

        if pdl_type == 'ELEC' and len(pdl) != 14:
            raise serializers.ValidationError("PDL must be a 14-digit")
        elif pdl_type == 'GAZ' and len(pdl) != 6:
            raise serializers.ValidationError("PDL must be a 6-digit")
        return validated_data
