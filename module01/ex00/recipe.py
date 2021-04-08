# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 19:56:28 2021

@author: KHEY HIBA
"""

import datetime
class Recipe:
    def __init__(self,name,cooking_lvl,cooking_time,ingredients,description,recipe_type):
        self.name=str(name)
        if(cooking_lvl in range(1,6)):
            self.cooking_lvl=cooking_lvl
        else:
            raise ValueError("Error")
        if not(isinstance(ingredients, list)):
            raise ValueError("It is not a list")
        if not(isinstance(cooking_time, int) and cooking_time>0):
            raise ValueError("Cooking time must be positive")
        if(recipe_type not in("starter", "lunch", "dessert")):
            raise ValueError("Error1")
        self.cooking_time=cooking_time
        self.ingredients=ingredients
        self.description=str(description)
        self.recipe_type=recipe_type
    def __str__(self):
        return f"The recipe name is {self.name}, it\'s a {self.recipe_type} it takes {self.cooking_time} minutes.\n Ingredients:{self.ingredients}"

