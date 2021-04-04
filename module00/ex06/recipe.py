cookbook={
          "Sandwich":{"ingredients":["ham","bread","cheese","tomatoes"],"meal":"lunch","prep_time":"10 minutes"},
          "Cake":{"ingredients":["flour","sugar","eggs"],"meal":"dessert","prep_time":"60 minutes"},
          "Salad":{"ingredients":["avocado","arugula","spinach"],"meal":"lunch","prep_time":"15 minutes"}
          }
def print_recipe(recipe_name):
    if recipe_name in cookbook:
        print("Recipe for:",recipe_name)
        print("Ingredients list: ",cookbook[recipe_name]["ingredients"])
        print("To be eaten for ",cookbook[recipe_name]["meal"])
        print("Takes ",cookbook[recipe_name]["prep_time"],"of cooking")
    else:
        print(recipe_name,"doesn\'t exist")    
def delete_recipe(recipe_name):
    if recipe_name in cookbook.keys():
        del(cookbook[recipe_name])
        print(recipe_name,"has been deleted")
    else:
        print(recipe_name,"doesn\'t exist")
def add_recipe(recipe_name,ingredients,meal,prep_time):
    cookbook[recipe_name]={"ingredients":ingredients,"meal":meal,"prep_time":prep_time}
    print(recipe_name,'has been added successfully')
def recipes_name():
    print("All recipes:\n")
    for i in cookbook.keys():
        print("The",i,"\'s recipe:\n")
        print("Ingredients list:",cookbook[i]["ingredients"])
        print("To be eaten for",cookbook[i]["meal"])
        print("It takes",cookbook[i]["prep_time"]," to prepare\n\n")

print("Please select an option by typing the corresponding number:\n1:Add a recipe\n2:Delete a recipe\n3:Print a recipe\n4:Print the cookbook\n5:Quit")
x=int(input("Option:\n"))  
while(x!=5):
    if(x>5 or x<1):
        print("This option doesn't exist, please type the corresponding number.\nTo exit enter 5\n")
        break
    if(x==4): 
        print(recipes_name())
    else:
        recipe_name=str(input("Please enter the recipe\'s name \n"))
        if(x==1):
            Ingredients=str(input("Please enter the ingredients"))
            Meal=str(input("Please enter the type of the meal"))
            Preparation_time=str(input("Please enter the preparation time needed"))
            add_recipe(recipe_name, Ingredients, Meal, Preparation_time)
        if(x==2):
            print(delete_recipe(recipe_name))    
        if(x==3):
            print(print_recipe(recipe_name))
    x=int(input("Option:\n"))
print("Exit")
