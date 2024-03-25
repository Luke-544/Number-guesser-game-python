import random

#r = random.randrange(0,21)#the randrange function will not include the upper limit
#r = random.randint(0,20)#the randint function includes the upper limi
number = input("Enter a number: ")

if number.isdigit():
    number = int(number) #this code check to confirm if the user inputed a digit or not
                         #If it was a digit, it will cast the input to a digit
                         #else the user will be prompted to input a digit

    if number <= 0:
        print("Please enter a higher number than zero next time")
        quit()  #this is an IF statement inside another IF statement to check if the input is less or equal to 0
else:
        print("You did not input any number")
        quit()

random_number = random.randint(0,number)
#print(random_number)

while True: #the while loop will keep prompting the user to make guesses
     user_guess = input("Make a guess: ")
     if user_guess.isdigit():
        user_guess= int(user_guess)
     else:
          print("You did not input any number")
          continue
     
     if user_guess ==random_number: #the user will make guesses until guessed number and the random number are equal
          print("Congratulations, you got it!!")
          break
     else:
          print("Try again")
