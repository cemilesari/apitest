from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from .models import Currencies
from .serializers import CurrenciesSerializer


class CurrenciesList(APIView):
    def get(self, request):
        curencies = Currencies.objects.all()
        serializer = CurrenciesSerializer(curencies, many=True)
        return Response(serializer.data)

    def post(self):
        pass
