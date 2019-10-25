# The operator will input the students name, type of student, percent score
# Based on the table below the program will use an if/else if/else structure
# with nested if staements and
# output the data in the following format.
# name, type of student, decimal grade, Letter grade, scholoarship status, student standing

# Conditions
# If a graduate student has an A or an A+
#    the Graduate student can continue receiving a scholarship
#    otherwise the scholarship is cancelled. 
# If an undegraduate is has a 3.4 or better
#    the Undergraduate student can continue receiving a scholarship
#    otherwise the scholarship is cancelled. 

# If a graduate student Falls below a 3.3
# The student is on probation otherwise the student is in good standing

#Tips
# Conditional Inputs:
#         name = Students first and last name.
#         percent_score = Students percent score.
#         type_student = ('G') for Graduate Student ('U') for undergradute student.
#         

#  Output
# name, type of student, decimal grade, Letter grade, scholoarship status, student standing

print("This program determines the students decimal grade")
print("Scholoarship status, Student standing")

# Prompting the user for values to the input variables
name = input("Please enter the students name:")
type_student = input("Please enter the students type 'G' or 'U':")
percent_score = float(input("Please enter the students percent score:"))



#Declare and intialize output variables
letter_grade = ''
renew_scholarship = 'Eligible'
decimal_grade = 0
student_standing = 'Good Standing'

print('\n' * 50)
#  using  if elif else
if percent_score >= 98.75:
    decimal_grade = 4.0
    letter_grade = 'A+'
elif 97.50 <= percent_score:
    decimal_grade = 3.9
    letter_grade = 'A+'
elif 96.25 <= percent_score:
    decimal_grade = 3.8
    letter_grade = 'A'
elif 95.00 <= percent_score:
    decimal_grade = 3.7
    letter_grade = 'A'
elif 93.75 <= percent_score:
    decimal_grade = 3.6
    letter_grade = 'A'
elif 92.50 <= percent_score:
    decimal_grade = 3.5
    letter_grade = 'A-'
    if type_student == 'G':
        renew_scholarship = 'Not Eligible'
elif 91.25 <= percent_score:
    decimal_grade = 3.4
    letter_grade = 'A-'
    if type_student == 'G':
        renew_scholarship = 'Not Eligible'
elif 90.00 <= percent_score:
    decimal_grade = 3.3
    letter_grade = 'A-'
    if type_student == 'G':
        renew_scholarship = 'Not Eligible'
    else: # Is an Under Grad
        renew_scholarship = 'Not Eligible'
else:
    if type_student == 'G':
        student_standing = 'Probation'
        decimal_grade = 'NA'
        letter_grade = 'Other'
print(name)
print("has a decimal grade of: ",decimal_grade)
print('the letter grade is: ',letter_grade)
print('The Scholarship Status is: ', renew_scholarship)
print('The Students Standing: ', student_standing)

input("Press Enter to Exit")