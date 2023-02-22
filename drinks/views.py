"""This is where you create all the endpoints for the API"""

"""Here, all the lists are drawn, analyzed through serializing, and a json object format is returned"""

from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def drink_list(request):
    # fetching the drinks
    # drinks = Drink.objects.all()

    # analyzing by serializing
    # serializer = DrinkSerializer(drinks, many=True)

    # return a json object
    # return JsonResponse({'drinks': serializer.data}, safe=False)

    try:

        if request.method == 'GET':
            drinks = Drink.objects.all()
            serializer = DrinkSerializer(drinks, many=True)
            return JsonResponse({'drinks': serializer.data}, safe=False)
        if request.method == 'POST':
            serializer = DrinkSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

    except SystemError as e:
        return 'Error: {0}'.format(e)


"""Creating the api endpoints"""
