from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers


class HelloAPIView(APIView):
    """Test API view"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format = None):
        """Return a list of APIView features"""
        an_apiview = [
        'Uses HTTP methods as function (get, put, post, patch, delete)',
        'Tapi Evan Ganteng banget :) '
        ]

        return Response({'massage' : 'hello', 'an_apiview' : an_apiview})

    def post(self, request):
        """Create a hello massage with user name"""
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            massage = f'Hello {name}'
            return Response({'massage' : massage})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk = None):
        """Handle updating an object"""
        return Response({'message' : 'PUT'})

    def patch(self, request, pk = None):
        """Handle partial update of an object"""
        return Response({'massage' : 'PATCH'})

    def delete(self, request, pk = None):
        """Delete an object"""
        return Response({'massage' : 'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """Test API View Set"""

    def list(self, request):
        """Return Hello"""
        a_viewset = [
            'viewset is use for actions(list, create, retrieve, update, partial_update)',
            'Automatic maps to URLs using Router',
            'Evan Ganteng'
        ]

        return Response({'massage' : 'Hello', 'a_viewset' : a_viewset})
