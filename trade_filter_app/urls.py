from django.urls import path
from .views import Trade_Details, TradeList

urlpatterns = [
    path('trades/', TradeList.as_view(), name='trade-list'),
    path('trades/create/', TradeList.as_view(), name='trade-create'),
    path('trades/<int:id>/', Trade_Details.as_view(), name='trade-detail'),
    path('trades/<int:id>/update/', Trade_Details.as_view(), name='trade-update'),
    path('trades/<int:id>/delete/', Trade_Details.as_view(), name='trade-delete'),
]



