from rest_framework import serializers

from sales.models import Sales


class SalesSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M", read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Sales
        fields = [
            'id',
            'book',
            'quantity',
            'total_price',
            'is_active',
            'is_deleted',
            'created_at',
        ]

    def get_total_price(self, obj):
        return obj.total_price()
