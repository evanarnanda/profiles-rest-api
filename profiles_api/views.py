from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


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

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return Hello"""
        a_viewset = [
            'viewset is use for actions(list, create, retrieve, update, partial_update)',
            'Automatic maps to URLs using Router',
            'Evan Ganteng'
        ]

        return Response({'massage' : 'Hello', 'a_viewset' : a_viewset})


    def create(self, request):
        """Create Hello massage"""
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

    def retrieve(self, request, pk = None):
        """Take an object by its id"""
        return Response({'HTTP_METHOD' : 'GET'})

    def update(self, request, pk = None):
        """Update an object"""
        return Response({'HTTP_METHOD' : 'PUT'})

    def partial_update(self, request, pk = None):
        """Update partialy of an object"""
        return Response({'HTTP_METHOD' : 'PATCH'})

    def destroy(self, request, pk = None):
        """Delete an object"""
        return Response({'HTTP_METHOD' : 'DELETE'})


class UserProfilesViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerilizer
    queryset = models.UserProfiles.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
