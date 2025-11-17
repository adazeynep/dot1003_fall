##task21
print("")
def greeting(name):
    print(f"Hello {name}")
user_input=input("Please type your name: ")
greeting(user_input)
##task22
print("")
def greeting2(name):
   return f"Hello {name}"
print(greeting2(user_input))
##task23
print("")
def sum(arg1,arg2):
    return arg1 + arg2
print(sum(3,2))
##task24
print("")
def greeting(input_name):
    print(f"Hi {input_name}")

    greeting("Andrew Ryan")
    greeting("Gordon Freeman")
##rask25
print("")
def mean(arg1,arg2,arg3):
 return (arg1 + arg2 + arg3)/3
print(mean(1, 2 , 3))
##task26

deger = True
while deger :
   isim = input("Say my name: ")
   if isim == "Heisenberg" :
      print("Youre goddamn right.")
      deger = False
##task27
print("")
my_flag = True
mypassword = input(" Enter your password: ")
while my_flag :
    myrealpassword = input("Enter again: ") 
    if mypassword == myrealpassword :
       print("Your password matches and account created successfully. ")
       my_flag = False
    else :
       print("They are not the same.")
##task28
print("")
number = int(input("Please enter a number: "))
my_flag = True
while my_flag : 
   print(number)
   number=number-1
   if number ==0:
     print("Kaboom ")   
     my_flag = False
##task29
print("")
correct_password=314159 
my_flag = True
attempts =3
while my_flag :
   user_input= int(input("Password: "))
   attempts= attempts-1
   if user_input == correct_password :
      my_flag= False
      print("Welcome ")
   elif attempts ==0 : 
      my_flag = False
      print("Incorrect password. Exerminate...")

   elif user_input != correct_password:
      my_flag = False 
      print("Try again. ")
##task31
print("")
my_list = [99,98,97]
print(my_list)
print(my_list[0])
print(len(my_list))
my_list.remove(98)
print(my_list)
##task32
print("")
my_list = [96,95,94]
print(my_list)
my_list[0]=100
print(my_list)
##task33
my_list=[]
my_flag= True
while my_flag:
 name= input("Please enter an input: ")
 if name == "exit" :
   my_flag= False
 else:
   my_list.append(name)
print(my_list)
##task34
print("")
my_list = ["Mahmut", "Agent 47", "Kratos", "Geodude", "Heisenberg"]
for i in my_list:
   print(i)
##task35
print("")
isim= input("Please enter an input: ")
for char in isim:
    print(char)
##task36
print("")
raw_points=[1,2,1,3]
print(f"total {sum(raw_points)} points earned.")
##task37
print("")
raw_points=[1, -2, 1,3,-5,7,0]
total_points=0
if i >0:
   total_points= i+total_points
   print(f"total {sum(raw_points)} points earned. ")
   






   
