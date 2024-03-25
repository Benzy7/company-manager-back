from rest_framework import serializers
from core.models import Company, Counter
from core.apis.counter.serializers import CounterSerializer
from core.apis.manager.serializers import ManagerSerializer
import re


class CompanyDetailSerializer(serializers.ModelSerializer):
    manager = ManagerSerializer(read_only=True)
    counters = serializers.SerializerMethodField()

    def get_counters(self, obj):
        counters_qs = Counter.objects.filter(company=obj)
        serializer = CounterSerializer(counters_qs, many=True)
        return serializer.data
    
    class Meta:
        model = Company
        fields = (
            "name",
            "reason",
            "siret",
            "postal_code",
            "manager",
            "counters",
        )
        read_only_fields = fields


class CompanySerializer(serializers.ModelSerializer):
    manager_first_name = serializers.CharField(source="manager.first_name", required=False)
    manager_last_name = serializers.CharField(source="manager.last_name", required=False)

    def validate_siret(self, value):
        if not re.match(r'^\d{14}$', value):
            raise serializers.ValidationError("Siret must be a 14 characters.")
        return value

    class Meta:
        model = Company
        fields = '__all__'
