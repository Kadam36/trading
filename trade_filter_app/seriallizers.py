from rest_framework import serializers
from . models import Trade

class TradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = ['id', 'trade_id', 'symbol', 'timeframe', 'target_1', 'target_2', 'stop_loss_1', 'stop_loss_2', 'create_time', 'update_time']