# 1.2 write a program that determines whether a year entered by the user is a leap year or not using the ifelifelse statements.

year = 2020

# to get year ( integer input ) from the user
# year = int(input("Enter a year: "))

# divided by 100 means century year (ending with 00)
# century year divded by 400 is leap year
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year)) 
  
# not divied by 100 means not century year
# year divded by 4 is leap year
elif (year % 4 == 0) and (year % 100 != 0):
    print("{0} is leap year".format(year))
  
# if not divied by both 400 (century year) and 4 ((not century year)
# year is not leap year
