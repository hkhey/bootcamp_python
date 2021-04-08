# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 20:00:39 2021

@author: KHEY HIBA
"""
import time
from datetime import datetime
from recipe import Recipe
class Book:
    """bhbhnhnhnhnhnh"""
    def __init__(self,name):
        self.name=name
        self.creation_date=datetime.now()
        self.last_update=datetime.now()
        self.recipes_list={"starter":[],"lunch":[],"dessert":[]}
    def get_recipe_by_name(self,name):
        for key in self.recipes_list.keys():
            for i in self.recipes_list[key]:
                if(i.name==name):
                    print(i)
                    return i
    def get_recipe_by_type(self, recipe_type):
        R=[]
        for i in self.recipes_list[recipe_type]:
            R.append(i.name)
        return R
    def add_recipe(self,recipe):
        self.last_update=datetime.now()
        self.recipes_list[recipe.recipe_type].append(recipe)



        
        