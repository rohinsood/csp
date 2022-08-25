# @author Rohin Sood

from colorama import Fore
import sys

"""
declare all questions & answers within a dictionary
key: question
value: answer
"""
question_answers = {
  "x\u00b2+3x+2": "(x+1)(x+2)", 
  "x\u00b2+x-6": "(x-2)(x+3)", 
  "a\u00b2-2a-35": "(a+5)(a-7)", 
  "3y\u00b2-15y+18": "3(y-2)(y-3)",
}

question_number = 0

correct_answers = 0

"""
print with the formatted colors & prefix
@param string - the string printed
"""
def format_print( string: str ):
  print( Fore.BLUE + "\q\> " + Fore.WHITE + string + Fore.WHITE)

"""
format the input prompt with colors & prefix
@param string - the string printed
"""
def format_input ( string: str ):
  return input( Fore.BLUE + "\q\> " + Fore.WHITE + string + Fore.WHITE)

"""
check if user answer is the same as the question answer
@param user_answer - the answer provided by the user
@param question - the key used to access the answer in questions_and_answers
"""
def check_answer( user_answer: str, question: str ):

  if (user_answer == question_answers[question]):
    return True
  else:
    return False

######
# Begin script!!
######

continue_quiz = format_input( Fore.GREEN + "Hello There!" + Fore.WHITE + " Are you ready to take this 4 question quiz on factoring polynomials? (y/n) ")

# exit the script if prompted
if continue_quiz != "y": 
  format_print( Fore.RED + "L goodbye")
  sys.exit()

# print example question and response
format_print("Example Question #0: x\u00b2-16")
format_print("Example Answer: (x+4)(x-4)")

format_print( Fore.RED + "Remember not to add spaces!!" )

# wait for user to be fully ready
format_input("(Press enter to start the quiz) ")

format_print( Fore.GREEN + "Have Fun!!" )

# iterate through items in question_answers
for question, answer in question_answers.items():

  # increase the question_number by one since indices
  question_number += 1

  # print the current question
  format_print("~~ Question #" + str(question_number) + ": " + question)

  # store the user answer
  user_answer = format_input( Fore.YELLOW + "Your Answer: ")

  if (check_answer(user_answer=user_answer, question=question)):

    format_print( Fore.GREEN + "Correct!" + Fore.WHITE )

    # increase correct answers by one
    correct_answers += 1
  
  else:

    # print the correct answer if user is incorrect
    format_print( Fore.RED + "Stupid ahh")
    format_print("The correct answer is: " + Fore.GREEN + answer)

# print % of answers correct & leave
format_print( Fore.GREEN + "Quiz Complete! " + Fore.WHITE + "You got " + str(correct_answers/4*100) + r"% of answers correct :)")