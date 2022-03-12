from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_app import serializers

class HelloApiView(APIView):

    """test API View"""
    serializer_class=serializers.HelloSerializer

    def get(self,request,format=None):
        """Return a list of APIView features"""
        an_apiview=[
        'uses HTTP methods as function (get,post,patch,put,delete)',
        'is similar to a traditional django view',
        'gives you the most control over you application logic',
        'is mapped manually to urls'
        ]

        return Response({'msg':'Hello!','an_apiview':an_apiview})

    def post(self,request):
        """Create a hello msg with our name"""
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            msg=f'Hello {name} '
            return Response({'msg':msg})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,pk=None):
         """handle updating an object"""
         return Response({'method':'put'})

    def patch(self,request,pk=None):
         """handle partially update on an object"""
         return Response({'method':'patch'})

    def delete(self,request,pk=None):
        """handle deletion operation on an object"""
        return Response({'method':'delete'}) 
