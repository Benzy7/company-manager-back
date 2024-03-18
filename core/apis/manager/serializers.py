from rest_framework import serializers
from core.models import Manager



class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'

    def validate_phone_number(self, value):
        if not value.isdigit() or len(value) != 8:
            raise serializers.ValidationError("Phone number must be a 8-digit number.")
        return value
