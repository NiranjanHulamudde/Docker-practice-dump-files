def function():
    return(2 + 2)

def f2():
    return(64 * 2)

def f3():
    return(15 / 3)



print(function() )
print("And") 
print(f2() )
print("And") 
print(f3())

print("The addition of above values is " + str(int(((function() + f2() + f3())))))


print("below is a random number")
import random
print(random.randint(1,10))

print(9 < 4)

print("Lets compare the user input of number to 10")

user_input = input("please enter a number ")

if int(user_input) > 10:
    print("The number is greater than 10")
elif int(user_input) < 10:
    print("the number is smaller than 10")
elif int(user_input) == 10:
     print("the number is equal to 10")

