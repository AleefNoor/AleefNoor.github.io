start = '''
You wake up one morning and find that you are running late. You skip breakfast and run out of the house. On your way you find a plastic bag lying on the ground.
There is a garbage can beside you. What do you do?
'''


print(start)

print("Type 'pickup' to pickup or 'continue' to go school.")
user_input = input()

if user_input == "pickup":
    print("You pick up the plastic bag and throw it into the garbage can.") 
    print("You are awesome. You just saved a panda.")
    print("You then walk to school. Unfortunately you reach school late. You reach school on lunch time. In lunch, your friend doesn't put his empty soda can in the recycle bin. He leaves it on the table. Do you tell him to put in the recycle bin or let it be?")
    user_input=input("Type 'tell' to tell your friend or 'leave' to let it be.")

if user_input == "tell":
	print("Your friend throws the soda can in the recycle bin. You are a superhero. You saved the planet!!") 
elif user_input == "leave":
	print("Oh well! You walk to class.") 
	# finished the story by writing what happens
 
elif user_input == "continue":
    print("You keep walking to school")
    print("You then walk to school. In comp sci, your teacher doesn't put his empty soda can in the recycle bin. He leaves it on the table. Do you ask him to put in the recycle bin or let it be?")
    user_input=input("Type 'ask' to tell your friend or 'leave' to let it be.")

if user_input == "ask":
	print("Your teacher gives you a cold look but throws it into the recycle bin.")
elif user_input == "leave":
	print("Oh well! You walk to class.") 
	

 