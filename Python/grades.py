

# Each of our grades
kristen_grades = [90, 85, 100, 77, 94]
clarisse_grades = [96, 83, 89, 97, 86]
sapna_grades = [82, 91, 94, 87, 99]

# Class grade book
grade_book = [kristen_grades, clarisse_grades, sapna_grades]

'''
This is what our grade book looks like
[	[90, 85, 100, 77, 94]
	[96, 83, 89, 97, 86]
	[82, 91, 94, 87, 99] ]

'''

# Traverse through the grade book and print all the indivdual grades
for individual in grade_book:
	for x in individual:
		print(x)

		
# Extensions: Find the class average, median, and standard deviation
# (For the extentions google for hints!)
add = (sum(kristen_grades) + sum(clarisse_grades) + sum(sapna_grades))//15
print("The avergae is " + str(add))
user_input=input("If you want the average of each of the three students, please type their name:  " )
if user_input=="kristen":
	Kristen= (sum(kristen_grades))//5
	print(Kristen)
elif  user_input=="clarisse":
	Clarisse= (sum(clarisse_grades))//5
	print(Clarisse)
elif user_input=="sapna":
	Sapna= (sum(sapna_grades))//5
	print(Sapna)
		

# Super extra extensions: calculate the student with highest/lowest average