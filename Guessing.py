# ----------imported random to take secret number as  random------------#
import random
# created secret number variable that takes secret number as random
secret_num = random.randint(1,15)
#maximum number of attempts that user can try
maximum_attempts = 3 
attempts = 1 # intially attempt is 1
#----- For admin access------#
Admin_password = "Admin119"
check = str(input("Are you admin(yes/no):")).lower()
# checks condition is true or not
if check == "yes":
    password = str(input("Enter password"))
    if Admin_password == password :
        print(f"Recognised as admin ,{secret_num}")
    else:
        print("Wrong password")

#---- loop continues until attempts is less than or equal to maximum attempts
while attempts <= maximum_attempts:
    user_guess = int(input("Enter correct guess between 1 to 15 : "))
    # checks whether condition is true or not
    if user_guess == secret_num:
        print("Congratulations,you have guessed corrected number  🎉")
        # loop breaks when condition is guess is correct
        break
     #  displays print statement when the uesr guess is less than secret number 
    elif user_guess < secret_num:
        print(f"Too low.Try again and remaining attempts left {maximum_attempts - attempts}")
     #   displays print statement when the uesr guess is less than secret number       
    elif user_guess > secret_num:
        print(f"Too high.Try again and remaining attempts left {maximum_attempts-attempts} ")
    # increments the attempts value by 1 when every time loop repeats
    attempts += 1
    # checks whether attempts are greater than maximum attempts 
    if attempts > maximum_attempts:
        print("Maximum attempts reached.please try again after 10 minutes")


