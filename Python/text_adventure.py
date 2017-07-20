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
    user_input=input("Type 'tell' to tell your friend or 'let go' to let it be.")

    if user_input == "tell":
        print("Your friend throws the soda can in the recycle bin. You are a superhero. You saved the planet!!") 
        print("After a long day in school, you are finally going home!!! On the road you encounter a suspicious guy. You see him leave a plastic lunch box on the road.")
        print("He looks left and right. He doesn't notice you. He then walks away. Something tells you that box isn't an ordinary box. You cross the road and take a look at the box.")
        user_input=input("Type 'open' to open the box or 'suspicious' to just walk home.")
        if user_input == "open":
            print("OMGGGGGG!!!!! YOU FOUND A THOUSAND DOLLARS IN THE LUNCH BOX!!")
            print("This is earth's reward to you for taking care of it.")
        elif user_input == "suspicious":
            print("Alas! Home sweet home!! You Dump your bag on the floor and you fall on the bed. You are tired. You decide to check your notifications on your phone.")
            print("As you scroll through your notifications, you see that you have two new emails. You check it out. One is from Columbia and the other from College Board.")
            user_input=input("Type 'columbia' to open the email from Columbia or 'board' to open the College Board email.")
            if user_input == "columbia":
                print("The email reads: Hey!! I am Joanna, a professor at Columbia. I walking down Pelt Avenue and I saw you putting the plastic bag in the right place. That was really nice of you. As I continued walking, I got a email from Columbia to pick candidates for the Columbia Computer Science program. Suprise, suprise, you were on the list. Your application was impressive.")
                print("So, I want to reward you. I have selected you, and I am happy to announce that you have been accepted into Columbia. Congrats!!")
            elif user_input == "board":
             print ("The email reads: You got 1520 in your recent SAT score!!!")
             print ("Congrats! Take care of earth and good karma will reward you!!")

    elif user_input == "let go":
        print("Oh well! You walk to class.") 
        print("School is over. You then go shopping. You have to buy new shoes and new clothes. Unfortunately, you don't have time for both. Which do you choose?")
        user_input=input("Type 'shoes' to go buy shoes or 'clothes' to buy clothes.")
        if user_input == "shoes":
            print("When you go shopping for shoes, you see there is a sale going on. When you check out your extra cool 100 dollar shoes, it's only 10 dollars!")
            print("This is good karma because you did the right thing for mother nature by telling the teacher to throw the can. Congrats")
        elif user_input == "clothes":
            print("When you go shopping for clothes, you see there is a sale going on. When you check out your extra cool 350 dollar dress, it's only 20 dollars!")
            print("This is good karma because you did the right thing for mother nature by telling the teacher to throw the can. Congrats!")


 
elif user_input == "continue":
    print("You then walk to school. In comp sci, your teacher doesn't put his empty soda can in the recycle bin. He leaves it on the table. Do you ask him to put in the recycle bin or let it be?")
    user_input=input("Type 'ask' to tell your friend or 'leave' to let it be.")
    if user_input == "ask":
        print("Your teacher gives you a cold look but throws it into the recycle bin.")
        print("School is over. You then go shopping. You have to buy new shoes and new clothes. Unfortunately, you don't have time for both. Which do you choose?")
        user_input=input("Type 'shoes' to go buy shoes or 'clothes' to buy clothes.")
        if user_input == "shoes":
            print("When you go shopping for shoes, you see there is a sale going on. When you check out your extra cool 100 dollar shoes, it's only 10 dollars!")
            print("This is good karma because you did the right thing for mother nature by telling the teacher to throw the can. Congrats")
        elif user_input == "clothes":
            print("When you go shopping for clothes, you see there is a sale going on. When you check out your extra cool 350 dollar dress, it's only 20 dollars!")
            print("This is good karma because you did the right thing for mother nature by telling the teacher to throw the can. Congrats")
    elif user_input == "leave":
        print("Oh well! You walk to class.") 
        print("After a long day, you start going home. On the way home, you drop into a manhole. You had to stay there for 3 hours until help came.")
        print("When you finally reached home. You fell asleep without taking a shower because you were so tired! Then you start dreaming. A ferocious angel appears in your dream It keeps on throwimg fireballs at you. ")
        print(" The angel says 'This is your punishment for not caring about mother nature.'")
        user_input=input("Will you take care of mother nature next time? 'yes' or 'no'?")
        if user_input== "yes":
            print("Good job!")
        elif user_input== "no":
            print("Karma will bite you!")

	

 