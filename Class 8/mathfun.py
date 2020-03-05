
def deposit(amount:float):
    assert (amount > 0), "sorry the amount deposited must be greater than 0"

value = (input("Enter an amount to depostit >")
deposit(float(value))


#secon exp
def deposit(amount: float):
    assert (amount > 0), "sorry the amount deposited must be greater than 0"


value = (input("Enter an amount to depostit >")
         try:
             deposit(float(value))
         except AssertionError as my_error:
             print(my_error)
         except Exception as my_error:
             print(my_error)

         deposit(float(value))


value
try:
    deposit(float(value))
except Exception as myerror:
    print(myerror)


#other examp
try:
    myval = 6/0
except Exception as my_error:
    Print(myerror)
print ("I reached here")