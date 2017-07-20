Side_Dishes = ["Daal","Mutton","Shrimp","Fillet Fish","Mixed Veg"]
Main  = ["Rice","Fried Rice", "Biryani","Pillow Rice","Parboiled Rice"," Pasta"]
Dessert= ["Pudding","Rice Pudding", "Egg Pudding","Sweet Rice", "Chocolate Bigy"]
import random
print(" Welecome to mysterious menu! Do you want a mysterious menu?")
a=input("If yes, type 'yes' and if 'no', GO AWAY!!")
if a=="yes":
	print("For side dish you have " + random.choice((Side_Dishes)))
	print("For main course you have " + random.choice((Main)))
	print("For dessert you have " + random.choice((Dessert)))