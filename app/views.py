from django.http import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import IAR


# Create your views here.
class v1(APIView):
    def post(self, request, format=None):
        self.data=request.data
        
        try:
            object_iar = IAR.objects.filter(tfn=self.data['tfn'])

            if object_iar:
                object_iar = object_iar.order_by('taxpayer_year')[0]

                diff_gross_income = abs(object_iar.gross_income - self.data['gross_income'])
                
                return Response({
                    'status_code': status.HTTP_200_OK,
                    'request_id':self.data['request_id'],
                    'match_status':True,
                    'income_result':diff_gross_income,
                })

            else:
                return Response({
                    'status_code': status.HTTP_404_NOT_FOUND,
                    'request_id':self.data['request_id'],
                    'match_status':False,
                    'income_result':None,
                })
        except:
            return Response({
                "status_code": status.HTTP_400_BAD_REQUEST,
                "error_msg": "request is bad, please recheck it!!"
            })



