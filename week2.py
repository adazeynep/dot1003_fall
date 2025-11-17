##task11
print("")
fahrenheit=float(input("Please type in a temperature(F): "))
celsius= (fahrenheit -32) * 5/9
print("f{fahrenheit} degrees Fahrenheit equals {celsius:.6f} degrees Celcius")
if celsius< 0:
    print("Brr! It's cold in here!")
#task12
print("")
hourly_wage=float(input("hourly wage: "))
hours_worked=float(input("hours worked: "))
day_of_the_week=input("day of the week: ")
if day_of_the_week == "sunday": 
    hourly_wage *=2 
daily_wage= hourly_wage * hours_worked 
print(f"Daily wage:{daily_wage:2f}liras")
#task13
print("")
age=int(input("How old are you: ")) 
if age < 18 :
    print("You can't play Dark Souls.") 
elif age >18: 
    print("Here is Dark Souls.Lol.")
if age > 44:
   print("You are too old for this sh*t.") 
#task14
print("")
first =int(input("Type the first number: "))
second=int(input("Type the second number: "))
if first > second:
    print(f"First one {first} is greater. ")
elif second > first:
    print(f"Second one {second} is greater. ")
else:
    print(f"These are equal {first} = {second}")
#task15
first_word =input("Type the first word: ")
second_word =input("Type the second word: ")
if first_word > second_word: 
    print(f"({first_word}) comes alphabetically last. ")
elif second_word > first_word:
    print(f"({second_word}) comes alphabetically last.")
else: 
    print(f"These are the same! ")
#task16
print("")
community=input("Which community do yyou belong to?: ")
if (community== "New California Republic " or
    community== "NCR" or
    community=="Brotherhood of Steel" or
    community=="Caesar's Leginion " or
    community=="Great Khans" or
    community=="Vault Dweller"):
     print("You are belong to Fallout Universe. ")
elif community!="" and community!= None:
    print("Nope, you are not belong to Fallout Lore.")
#task17
print("")
points=int(input("How many points [0-100]: "))
if points<0:
    print("you what? ")
elif points<=49:
    print("Fail. ")
elif points >=50 and points <=59:
    print("1")
elif points >=60 and points <=69:
    print("2")
elif points >=70 and points <=79:
    print("3")
elif points >=80 and points <=89:
    print("4")
elif points >=90 and points<=100:
    print("5")
else: points>100 
print("Impossible!")
#task18
print("")
number=int(input("Enter number: "))
if number%15==0:
    print("FizzBuzz")

elif number%5==0:
    print("Buzz")

elif number%3==0:
    print("Fizz")
#task19
print("")
number=int(input("Please type in number: "))
if number >0 and number%2==0:
    print("The number is even")
else:
    print("The number is odd.")
#task20
print("")
year=int(input("Please type in a year"))
if year %100==0:
    print("That year is not a leap year.")
elif year%400==0: 
    print("That year is a leap year.")





