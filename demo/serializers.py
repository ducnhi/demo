from rest_framework import serializers

from demo.models import OrderModels


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderModels
        fields = ('country', 'tracking_number', 'seller_id', 'create_time', 'updated_time')
