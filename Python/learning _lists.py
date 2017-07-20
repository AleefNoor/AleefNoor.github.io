names= ["Joly","Dina","Gogo","Momo","Fofo","Grace", "Aleef","Nur","Reice","Anjali" ]
import random
print("Do you want a random name?")
user_input= input("Type 'yes' if you want a name or 'no' if you don't.") 
if user_input=="yes":
	print(random.choice(names))
