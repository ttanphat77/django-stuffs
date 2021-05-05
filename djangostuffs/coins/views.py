from rest_framework.response import Response
import yfinance as yf

# Create your views here.
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_coin(request):
    data = yf.download(tickers='BTC-USD', period='24h', interval='15m')
    return Response(data)