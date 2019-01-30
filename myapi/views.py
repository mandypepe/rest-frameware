from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import  status
from . import serializers
from .models import UserProfile
from django.http import HttpResponse, JsonResponse


# Create your views here.

class ApiViews(APIView):
    serializers_class=serializers.Serializer


    def get(self,request,format=None):
        """Retorna la lista """
        #api_view=UserProfile.object.all()
        api_view = ["mostrar esta ","esto","estootro"]
        return Response(api_view)

    def post(self,request):
        serializer=serializers.Serializer(data=request.data)
        if serializer.is_valid():
            name=serializer.data.get('name')
            message='Hello {0}'.format(name)
            return Response({'saludo':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,pk=None):
        """update obj entero"""
        return Response({"mensaje":"updateaste"})

    def patch(self,request,pk=None):
        """update solo los elementos mandados por el request"""
        return Response({'message':"update via patch"})

    def delete(self,pk=None):
        """Eliminar """
        return Response({"message":'delete'})
