import csv
import random

def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*','/'])
    question = "What is {} {} {}?".format(num1, operator, num2)
    answer = eval("{} {} {}".format(num1, operator, num2))
    return question, answer

def take_quiz():
    name = input("Enter your name: ")
    questions = [generate_question() for _ in range(5)]

    correct_answers = 0
    for question, answer in questions:
        user_answer = int(input(question + " "))
        if user_answer == answer:
            print("Correct!")
            correct_answers += 1
        else:
            print("Wrong! The correct answer is :",answer)

    percentage = (correct_answers / 5) * 100
    

    file = open('quiz_results.csv','a')

    output = ([name, answer, 'out of',correct_answers, '/5', percentage,'%'])
    file.write(output)
    file.close()
    print("Quiz completed. You got {} correct! {} out of 5 questions correct.".format(answer, correct_answers))

def view_csv():
    file = open('quiz_results.csv','r')
    for row in file:
        print(row)
    file.close()

while True:
    print("\nMenu:")
    print("1. Take quiz")
    print("2. View results(from CSV)")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        take_quiz()
    elif choice == '2':
        view_csv()
    elif choice == '3':
        print("thanks for using the program. Goodbye!")
        break
    else:
        print("Please enter a number between 1 and 3.")