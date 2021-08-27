from django.http import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import IAR

# Create your views here.

class v1(APIView):
    def post(self, request, format=None):
        
        data=request.data
        
        object_iar = IAR.objects.filter(tfn=data['tfn'])

        if object_iar:
            object_iar = object_iar.order_by('taxpayer_year')[0]

            diff_gross_income = abs(object_iar.gross_income - data['gross_income'])
            
            return Response({
                'request_id':data['request_id'],
                'match_status':True,
                'income_result':diff_gross_income,
            })

        else:
            return Response({
                'request_id':data['request_id'],
                'match_status':False,
                'income_result':None,
            })



