import yfinance as yf
from rest_framework.response import Response
from rest_framework.views import APIView

class CoinView(APIView):
    def get(self, request, *args, **kwargs):
        data = yf.download(tickers='BTC-USD', period='24h', interval='15m')
        return Response(data)