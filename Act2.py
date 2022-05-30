import random

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

#number of problems
amount = int(input("How many problems to solve?: "))
#what operation to be used
print("            Operation Options: ")
print("1. Addition (+)          3. Multiplication (x)")
print("2. Subtraction (-)       4. Division (/)")
choice = input("Your choice: ")
score = 0
for i in range(amount): 
    if choice in ('1', '2', '3', '4'):
        if choice == '1':
            num1 = float(random.randint(0, 9))
            num2 = float(random.randrange(2, 10, 2))
            sum = add(num1, num2)
            print("What is the sum of " + str(num1) + " and " + str(num2))
            answer = float(input("Enter your answer: "))
            if sum == answer:
                print ("Correct")
                score += 1
            else:
                print("Wrong! the correct answer is ", sum)
        
        elif choice == '2':
            num1 = float(random.randint(0, 9))
            num2 = float(random.randrange(2, 10, 2))
            diff = subtract(num1, num2)
            print("What is the difference of " + str(num1) + " and " + str(num2))
            answer = float(input("Enter your answer: "))
            if diff == answer:
                print ("Correct")
                score += 1
            else:
                print("Wrong! the correct answer is ", diff)

        elif choice == '3':
            num1 = float(random.randint(0, 9))
            num2 = float(random.randrange(2, 10, 2))
            total = multiply(num1, num2)
            print("What is the total of " + str(num1) + " and " + str(num2))
            answer = float(input("Enter your answer: "))
            if total == answer:
                print ("Correct")
                score += 1
            else:
                print("Wrong! the correct answer is ", total)

        elif choice == '4':
            num1 = round(float(random.randint(0, 9)), 2)
            num2 = round(float(random.randrange(2, 10, 2)), 2)
            div = divide(num1, num2)
            print("What is the dividend of " + str(num1) + " and " + str(num2))
            answer = float(input("Enter your answer: "))
            if div == answer:
                print ("Correct")
                score += 1
            else:
                print("Wrong! the correct answer is ", div)

        
print("Your Score: ", score)
