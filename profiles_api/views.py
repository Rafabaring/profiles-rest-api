from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status # usado na post function

from profiles_api import serializers

from profiles_api import tests

class HelloApiView(APIView):
    """Test API View"""
    # Configura esta class HelloApiView para user o serializer correto
    serializer_class = serializers.HelloSerializer


    def get(self, request, format = None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put delete)',
            'Is similar to traditional Django view',
            'Giver you the most control over your application logic',
            'Is mapped manually to URLs'
        ]

        printing_test = tests.imprimindo()

        return Response({'message' : 'Hello',
                         'an_apiview': an_apiview,
                         'imprimindo': printing_test})


    def post(self, request):
        """Create a hello message with name"""
        serializer = self.serializer_class(data = request.data)

        # .is_valid() verifica se o serializer segue os parâmetros iniciais. Nesse caso, max_length = 10
        if serializer.is_valid():
            name = serializer.validated_data.get('name') # name é o nome da variavel no arquivo serializer
            message = f'Hello {name}'

            x = serializer.validated_data.get('x')
            y = serializer.validated_data.get('y')
            x_y_multiplied = tests.multiplier(x, y)

            return Response({'message': message,
                             'x and y multiplied': x_y_multiplied})

        # Se o dado não for valid (acima), vai retornar um http bad request
        else:
            return Response(
                    serializer.errors,
                    status = status.HTTP_400_BAD_REQUEST
                )


    def put(self, request, pk = None):
        """
        Handle updating an object
        """
        return Response({'method': 'PUT@'})


    def patch(self, request, pk = None):
        """
        Handle a partial update of an object
        """
        return Response({'method': 'PATCH@'})


    def delete(seld, request, pk = None):
        """
        Delete an object
        """
        return Response({'method': 'DELETE@'})
