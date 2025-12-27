##task67
def coordinator(arg1,arg2):
    my_coordinates=(5,6)
    print(my_coordinates)
  
coordinator(5,6)

##task68

my_coordinates = {}
def coordinator(x,y): 
    return(x,y)

my_coordinates[coordinator(0,0)] = "Home"
my_coordinates[coordinator(1,1)] = "Work"
my_coordinates[coordinator(-1,-1)] = "School"

for k,v in my_coordinates.items():
    print(f"position: {k} name: {v}")

##task69
weapons=[("blade",10),("sabre", 35), ("sword",50)]

def print_best_weapon(weapons):
    max_power=0
    meele_weapon=" "
    for weapon in weapons:
        if weapon[1]>max_power:
            max_power=weapon[1]
            meele_weapon=weapon[0]
    print(meele_weapon)
print_best_weapon(weapons)

##task70
game_table=[['_','_','_'],['_','_','_'],['_','_','_']]
user_input=[]
def coordinator(x,y):
    return(x,y)

my_flag=True
while my_flag:
    if user_input=="exit":
        my_flag=False
    else:
        x=int(input("Please enter x: "))
        y=(input("Please enter y: "))
user_coordinates=coordinator(x,y)
user_input.append(user_coordinates)

for user_coordinates in user_input:
    row = user_coordinates[0]  
    col = user_coordinates[1]

game_table[row][col] = '*'
for row in game_table:
    print(row)

##task71
my_set=set()
my_flag=True
while my_flag:
    user_input=input("Enter a element for set: ")

    if user_input=="exit":
        my_flag=False
    else:
        my_set.add(user_input)

for item in my_set:
    print(item)
           
##task72
my_set=set()
my_flag=True
while my_flag:
    user_input=input("Enter a element for set: ")

    if user_input=="exit":
        my_flag=False
    else:
        if user_input in my_set:
            print(f"{user_input} is already in our set.")
        else:
            my_set.add(user_input)
        
print(my_set)

##task73
local_variables=["my_ans"]
global_variables=["real_age","name", "user_guess","question"]

##task75
def start_game(): 
    global score
    score = 10 
    print(f"Game started! Current score: {score}")

def increase_score(): 
    global score 
    score+= 5 
    print(f"Score increased! Current score: {score}")

def display_score(): 
    print(f"Final score: {score}")

score = 0
start_game()
increase_score() 
display_score()

##task76
def age_calc():
 my_flag=True
 while my_flag:   
        try:
            birth_year=int(input("Please enter your birthyear: "))
            age=2025 - birth_year
            return age
        
        except ValueError:
            print("Invalid Input. Enter again: ")
 
print(f"You are {age_calc()} years old.")
    
##task77
x = int(input("Please enter a number: "))
flag = True
while flag:
    try:
        y = int(input("Please enter divider: "))
        print(f"{x} divided by {y} is {x / y}")
        flag = False
    except SyntaxError:
            print("Some kind of error occured")
    except ZeroDivisionError:
            print("You cant enter 0 as divider")
    except ValueError:
            print("Invalid Value")
##excep'in ardindan syntaxError gelmesi gerekiyordu sanırım?

##task79
def factorial(n):
    if n <0:
        raise ValueError("No negative value")
    k=1
    for i in range(2,n+1):
        k *=i
    return k
try:
    print(factorial(5))

    print(factorial(-1))
except ValueError as error_message:
    print(f"Error: {error_message}")



                   