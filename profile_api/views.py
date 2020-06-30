from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profile_api import serializers

class HelloApiView(APIView):
    """Test API view"""
    serializer_class = serializers.HelloSerializer
    def get(self,request,format=None):
        """Return a list of APIView features"""
        an_apiview = [
            'Users HTTP methods as function (get,post,patch,post,delete)',
            'Is similar to the traditional django view',
            'Gives you the full control over your applicatio logic',
            'is mapped mabually to URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({'message': message})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request, pk=None):

        return Response({'method': 'PUT'})

    def patch(self,request, pk=None):

        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        return Response({'method': 'DELETE'})
