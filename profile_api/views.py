from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API view"""
    def get(self,request,format=None):
        """Return a list of APIView features"""
        an_apiview = [
            'Users HTTP methods as function (get,post,patch,post,delete)',
            'Is similar to the traditional django view',
            'Gives you the full control over your applicatio logic',
            'is mapped mabually to URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
