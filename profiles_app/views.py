from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """test API View"""

    def get(self,request,format=None):
        """Return a list of APIView features"""
        an_apiview=[
        'uses HTTP methods as function (get,post,patch,put,delete)',
        'is similar to a traditional django view',
        'gives you the most control over you application logic',
        'is mapped manually to urls'
        ]

        return Response({'msg':'Hello!','an_apiview':an_apiview})
