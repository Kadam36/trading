from django.db import models

# Create your models here.
from django.db import models
import uuid

class Trade(models.Model):
    # 1. Trade id (UUID)
    trade_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    # 2. Symbol (string)
    symbol = models.CharField(max_length=100)

    # 3. Timeframe (enum - 15m, 1h, 4hr)
    class Timeframe(models.TextChoices):
        FIFTEEN_MINUTES = '15m', '15minutes'
        ONE_HOUR = '1h', '1hours'
        FOUR_HOURS = '4hr', '4hours'
        ONE_DAY = '1d','1day'

    timeframe = models.CharField(
        max_length=3,
        choices=Timeframe.choices,
        default=Timeframe.ONE_HOUR,
    )

    id = models.AutoField(primary_key=True)

    # 4. Target 1 (float)
    target_1 = models.FloatField()

    # 5. Target 2 (float)
    target_2 = models.FloatField()

    # 6. Stop Loss 1 (float)
    stop_loss_1 = models.FloatField()

    # 7. Stop Loss 2 (float)
    stop_loss_2 = models.FloatField()

    # 8. Create time (datetime)
    create_time = models.DateTimeField(auto_now_add=True)

    # 9. Update time (datetime)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Trade {self.trade_id} - {self.symbol} ({self.timeframe})"
