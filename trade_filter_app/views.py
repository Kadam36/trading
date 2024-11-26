from django.shortcuts import render
from .models import Trade 
from .seriallizers import  TradeSerializer
from django.shortcuts import get_object_or_404 
from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import status 
from rest_framework.exceptions import NotFound



class Trade_Details(APIView):
    def get_object(self,id):
        try:
            prd = Trade.objects.get(id=id)            
            return prd
        
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        

    def get(self,request,id):
            prd = self.get_object(id)
            serializer = TradeSerializer(prd)
            return Response(serializer.data,status=status.HTTP_200_OK)
        

   


    def delete(self, request, id):
        try:
            prd = self.get_object(id)
            prd.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)  # Deletion successful
        except NotFound:
            return Response(status=status.HTTP_404_NOT_FOUND)  #if the  Resource is not found
 

    def put(self,request,id):
        prd = self.get_object(id)
        serializer = TradeSerializer(prd,data=request.data)

        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class Student_list(APIView):    
    def get(self,request):
        
        prds = Trade.objects.all()
        serializer = TradeSerializer(prds,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)



    def post(self,request):        
        serializer = TradeSerializer(data=request.data)
        if(serializer.is_valid()):
    
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)



class TradeList(APIView):
    def get(self, request):
        trades = Trade.objects.all()
        serializer = TradeSerializer(trades, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TradeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)