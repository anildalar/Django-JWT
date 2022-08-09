from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class HelloView(APIView):
    #1. Property
    permission_classes = (IsAuthenticated,)
    
    #3. Method
    def get(self,request):
        content = {'message': 'Hello, World!'}
        return Response(content)
    pass
