from django.db import models
import os


class Drink(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    def __str__(self):
        jina = self.name
        scribe = self.description

        details_file = open('drinkdetails.txt', 'w')
        details_file.write(str(jina))
        details_file.close()

        with open('drinkdetails.txt', 'r') as drinkDetails:
            lines = drinkDetails.read()
            print(lines)

        return f"{jina}, {scribe}"
