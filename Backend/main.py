from Backend.FoodProcessor import FoodProcessor

favorite_color = ""
favorite_color_list = [""]
while(favorite_color != "0"):
    favorite_color = input("What is your favorite color")
    favorite_color_list.append(favorite_color)

def ask_stlye_type():
    style_type = input("Please enter your Style")
    return style_type

if __name__ == "__main__":
    user_style = ask_stlye_type()
    print ("Your Style type is:", user_style)
    food = FoodProcessor()
    food.generateRecipes("Paneer")
    uriList = food.getUriList()
    nameList =food.getNameList()
    print(nameList)