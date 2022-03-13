from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from profiles_app import serializers
from profiles_app import models
from profiles_app import permissions


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


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class=serializers.HelloSerializer

    def list(self,request):
        """Return a hello msg"""

        a_viewset={
        'uses actions (list,create,retrieve,update,partial_update)',
        'Automatically maps to URLs using Router',
        'Provides more functionality with less code',
        }

        return Response({'msg':'Hello!','a_viewset':a_viewset})

    def create(self,request):
        """Create a new Hello Msg"""
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            msg=f'Hello {name}!'
            return Response({'msg':msg})

        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        """Handles getting an object by its ID"""
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        """Handles updating an object"""
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        """Handle updating part of an object"""
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        """Handle removing an object"""
        return Response({'http_method':'DELETE'})


class UserProfileViewset(viewsets.ModelViewSet):
    """Handle Creating and Updating profiles"""
    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes=[TokenAuthentication,]
    permission_classes=[permissions.UpdateOwnProfile,]
    filter_backends = [filters.SearchFilter,]
    search_fields = ['name','email',]
