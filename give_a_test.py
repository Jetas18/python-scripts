import os


test_link = input("Enter the link for the past paper\n\n> ")


paper_code = input("Enter the year and month of the paper in format (year_month)\n\n> ")


subject = str(input("Enter the subject\n\n> ")).lower()


if not os.path.exists(subject):
    os.mkdir(subject)



marks = 0


number_of_questions = int(input("\n\n\nHow many questions are there?\n\n> "))

correct_answers = [] 

marking_scheme_answers = []

wrong_answers = []

answers = []

def get_answers(amount_of_questions, answer_array, message):

    i = 0
    print("\n\n\n")

    while i < amount_of_questions:
        temp = str(input( f"{message} {i+1}\n\n> ")).upper()
        
        if temp not in ["A", "B", "C", "D"]:
            print("Enter a valid option! \n\n\n")
        
        else:
            answer_array.append(temp) 
            print("\n\n\n")
            i += 1
    
get_answers(number_of_questions, answers, "Enter your answer for question number")


print("\n\n\n")


get_answers(number_of_questions, marking_scheme_answers, "Enter the correct answer on the marking scheme")






for i in range(0,number_of_questions):
    if answers[i] == marking_scheme_answers[i]: 
        marks += 1
    else:
        wrong_answers.append(int(i+1))
        correct_answers.append(marking_scheme_answers[i])





final_message = ""

for i, j in zip(wrong_answers, correct_answers):

    final_message += f" question number {i}, with the correct answer being {j}, you entered {answers[i-1]}\n\n"
    


if final_message == "":
    print("YOU ARE A GENIUS!!! YOU GOT ALL QUESTIONS CORRECT!")


else:
    print(f"You got {len(wrong_answers)} wrong answers\n\n")
    print(final_message)

    


print(f"\n\nYour final result is {marks}/{number_of_questions} and for percentage you got {round((marks/number_of_questions) * 100, 2 )}%")

last_line = f"\n\nYour final result is {marks}/{number_of_questions} and for percentage you got {round((marks/number_of_questions) * 100, 2 )}%" 

file_message = f"""link for the test paper-  {test_link}\n\n\n"""

for i, j, k in zip(answers, marking_scheme_answers, range(1,number_of_questions+1)):
     
    if i == j:
        file_message += f"{k}. {i}\n\n"
    else:
        file_message += f"{k}. {i}  X   {j}\n\n"


file_message += f"\n\n{final_message}\n{last_line}"


f =  open(f"{subject}/{paper_code}.txt", "w")


f.write(file_message)
