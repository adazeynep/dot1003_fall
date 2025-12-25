##task53
def spruce () :
    height=int(input(" Please enter a number for spruce height:"))
    box=int(input("Please enter a number for box size."))

    spruce_width=2 * height - 1
    if box < spruce_width:
        print("Box size couldn't be smaller than the spruce.")
        return
    print("-" * box)
    print("|" + " " * box +"|")
    for i in range(1, height+ 1):
        stars="*" * (2*i - 1)
        padding= box - len(stars)

        left= padding //2  
        right=padding - left
        print("|" + " "*left + stars + " " *right +"|")

    print("-" * box ) 
spruce()
    
##task54
text="The quick brown fox jumps over thee lazy dog "
search_item=input("Whic item do you want to search? ")
count=text.count(search_item)
print(f"Item {search_item} appeared {count} times. ")

##task55
def game_func():
 game=input("Enter the input to search: ")
 search_item=input("Which item do you wnt to search? ")
 result=game.count(search_item)
 print(f"Item {search_item} appeared {result} times.  ")
game_func()

##task56
def remove_vowels(menu_button):
    menu_button=""
    vowels="aeiouAEIOU"
    
    for char in menu_button:
        if char not in vowels:
            menu_button+=char
    return menu_button
user_text=input("Enter your sentence: ")
result=remove_vowels(user_text)
print("Without vowels:" ,result)

##task57
def anarya(game_list):
   game_list.reverse()
   return game_list
game_list=["Doom", "Max Payne","FTL"]
print(game_list)
reversed_list=anarya(game_list)
print(reversed_list)

##task58
game_list=[]
my_flag=True
def anarya(game_list):
    return game_list[::-1]

while my_flag:
    user_input=input("Enter an input: ")
    if user_input=="exit":
        my_flag=False
    else:
        game_list.append(user_input)
print(game_list)
print(anarya(game_list))


##task59
def longest_name(game_list):
    return max(game_list, key=len)
game_list=["Doom", "Max Payne", "FTL"]
print(game_list)
print(longest_name(game_list))                                                                                                                                 

##task60
my_matrix=[[1,2,3], [4,5,6], [7,8,9]]
element=int(input("Item to search: "))

def finder(my_matrix,element):

 for row in my_matrix:
   print(row)
print(finder(my_matrix,element))
if element in my_matrix:
  print(f"find at {row}, {column}")
  
finder(my_matrix,element)

##task61
def sum_of_row(my_matrix, row_no):
    
    selected_row=my_matrix[row_no]
    total=sum(selected_row)
    return total

my_matrix=[[1,2,3], [4,5,6],[7,8,9]]
element=int(input("row no: "))
for row in my_matrix:
    print(row)
result=sum_of_row(my_matrix,element)
print(f"Sum: {result}")
##task62

def sum_of_column(my_matrix,column_no):

    selected_column=my_matrix[column_no]
    total=sum(selected_column)
    return total

my_matrix=[[1,2,3], [4,5,6],[7,8,9]]
element=int(input("column no: "))

for column in my_matrix:
    print(column)
result=sum_of_column(my_matrix,element)
print(f"sum: {result}")

##task63
my_lucky_numbers=[4,8,15,16,23,42]
tripled_list=[]
def tripler():
    for i in my_lucky_numbers:
        numbers= i * 3
        tripled_list.append(numbers)

print(f"my lucky numbers {my_lucky_numbers}")
tripler()
print(f"tripled numbers {tripled_list}")

##task64
my_dictionary={
    "item1": 3,
    "item2": 1,
    "item3":5
}
for item, quantity in my_dictionary.items():
    print(f"{item}: {quantity}")

##task65
def add_item(item,quantity):
    if item in my_dictionary:
        my_dictionary[item] +=quantity
    else:
        my_dictionary[item] = quantity
my_dictionary={"item1":3,"item2":1,"item3":5}
add_item("item1",5)
add_item("item4",1)

for key,value in my_dictionary.items():
    print(f"{key}:{value}")

##task66
my_dictonary={
    "item1":3,
    "item2":1,
    "item3":5
}

def add_item(item,quantity):
    if item in my_dictionary:
        my_dictionary[item]+=quantity
    else:
        my_dictionary[item]=quantity
for key in my_dictionary:
    print(f"{key}: {my_dictionary[key]}")

def remove_item(item,quantity):
        if item in my_dictionary:
           my_dictionary[item] -= quantity
        if my_dictionary[item] < 0:
           my_dictionary[item] = 0

add_item("item1", 5)
add_item("item4", 1)

remove_item("item4", 6)
remove_item("item1", 2)

for key in my_dictionary:
    print(f"{key}: {my_dictionary[key]}")