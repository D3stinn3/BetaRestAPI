"""This is where you create all the endpoints for the API"""

"""Here, all the lists are drawn, analyzed through serializing, and a json object format is returned"""

from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer


def drink_list(request):
    # fetching the drinks
    drinks = Drink.objects.all()

    # analyzing by serializing
    serializer = DrinkSerializer(drinks, many=True)

    # return a json object
    return JsonResponse(serializer.data, safe=False)
